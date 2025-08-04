import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import settings
import tempfile


def run_app():
    # Check if user is logged in
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                       color: white; padding: 2rem; border-radius: 15px; text-align: center;">
                <h2 style="margin: 0;">🔒 Access Restricted</h2>
                <p style="margin: 0.5rem 0;">Please login first to access the detection system.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔐 Go to Login Page", use_container_width=True):
                st.session_state.page = "login"
        return

    @st.cache_resource
    def load_model(path):
        return YOLO(str(path))

    model = load_model(settings.DETECTION_MODEL)

    def classify_items(detected_items):
        r = set(detected_items) & set(settings.RECYCLABLE)
        nr = set(detected_items) & set(settings.NON_RECYCLABLE)
        h = set(detected_items) & set(settings.HAZARDOUS)
        o = set(detected_items) & set(settings.ORGANIC)
        b = set(detected_items) & set(settings.BIODEGRADABLE)
        return r, nr, h, o, b

    def show_sidebar_results(r, nr, h, o, b, all_detected):
        if not all_detected:
            st.sidebar.markdown("""
                
            """, unsafe_allow_html=True)
            return
 
        # Sidebar header
        st.sidebar.markdown("""
            <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
                       color: white; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                <h3 style="margin: 0; text-align: center;">🧾 Detection Results</h3>
            </div>
        """, unsafe_allow_html=True)

        # Summary statistics
        total_items = len(all_detected)
        st.sidebar.markdown(f"""
           
        """, unsafe_allow_html=True)

        # Categories with items
        categories_data = [
            (r, "♻️ Recyclable", "#e8f5e8", "#4CAF50"),
            (nr, "🚫 Non-Recyclable", "#ffebee", "#f44336"),
            (h, "☣️ Hazardous", "#fff3e0", "#ff9800"),
            (o, "🍃 Organic", "#f3e5f5", "#9c27b0"),
            (b, "🌱 Biodegradable", "#e0f2f1", "#00bcd4")
        ]

        for items, category_name, bg_color, border_color in categories_data:
            if items:
                st.sidebar.markdown(f"""
                    <div style="background: {bg_color}; padding: 1rem; border-radius: 8px;
                               border-left: 3px solid {border_color}; margin-bottom: 1rem;">
                        <h4 style="color: {border_color}; margin: 0 0 0.5rem 0; font-size: 1rem;">
                            {category_name} ({len(items)})
                        </h4>
                """, unsafe_allow_html=True)

                for item in sorted(items):
                    item_name = item.replace("_", " ").title()
                    disposal = settings.DISPOSAL_METHODS.get(item, "No disposal info available.")

                    st.sidebar.markdown(f"""
                        <div style="background: white; padding: 0.7rem; border-radius: 6px;
                                   margin-bottom: 0.4rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                            <strong style="color: #333; font-size: 0.9rem;">📦 {item_name}</strong><br>
                            <span style="color: #666; font-size: 0.8rem;">
                                🗑️ <em>{disposal}</em>
                            </span>
                        </div>
                    """, unsafe_allow_html=True)

                st.sidebar.markdown("</div>", unsafe_allow_html=True)

     

    def predict_and_display(image):
        results = model.predict(image, conf=0.4)
        detected = set(model.names[int(c)] for r in results for c in r.boxes.cls) if results else set()
        r, nr, h, o, b = classify_items(detected)

        if results:
            annotated = results[0].plot()
            st.image(annotated, channels="BGR", use_column_width=True)
        else:
            st.image(image, channels="BGR", use_column_width=True)

        show_sidebar_results(r, nr, h, o, b, detected)

    # Session state
    if "webcam_on" not in st.session_state:
        st.session_state.webcam_on = False
    if "last_frame" not in st.session_state:
        st.session_state.last_frame = None
    if "detected_r" not in st.session_state:
        st.session_state.detected_r = set()
    if "detected_nr" not in st.session_state:
        st.session_state.detected_nr = set()
    if "detected_h" not in st.session_state:
        st.session_state.detected_h = set()
    if "detected_o" not in st.session_state:
        st.session_state.detected_o = set()
    if "detected_b" not in st.session_state:
        st.session_state.detected_b = set()
    if "detected_all" not in st.session_state:
        st.session_state.detected_all = set()

    # Show initial sidebar state
    show_sidebar_results(
        st.session_state.detected_r,
        st.session_state.detected_nr,
        st.session_state.detected_h,
        st.session_state.detected_o,
        st.session_state.detected_b,
        st.session_state.detected_all,
    )

  

    # Header Section
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
            <h2 style="margin: 0; text-align: center;">AI Waste Detection System</h2>
            <p style="text-align: center; font-size: 1.2rem; margin: 0.5rem 0 0 0;">
                Upload an image or use your camera to identify and classify waste items
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Navigation and User Info
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 1rem; border-radius: 10px;
                   box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 2rem;">
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("🏠 Back to Home", key="home_from_app", use_container_width=True):
            st.session_state.page = "home"
    with col2:
        st.markdown("""
            <div style="text-align: center; padding: 0.5rem;">
                <span style="background: #4CAF50; color: white; padding: 0.3rem 1rem;
                           border-radius: 20px; font-size: 0.9rem;">
                    ✅ Logged in as: admin
                </span>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        if st.button("🚪 Logout", key="logout_from_app", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.page = "home"
            st.success("Logged out successfully!")

    st.markdown("</div>", unsafe_allow_html=True)

    # Image Upload Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #4CAF50; margin-top: 0;">📤 Upload Image for Analysis</h2>
            <p style="color: #666; margin-bottom: 1rem;">
                Select an image file (JPG, JPEG, PNG) to detect and classify waste items
            </p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_img = st.file_uploader(
        "Choose an image file",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image containing waste items for best results"
    )

    if uploaded_img:
        file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        predict_and_display(img)


        # Video Upload Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #FF9800; margin-top: 0;">🎥 Upload Video for Analysis</h2>
            <p style="color: #666; margin-bottom: 1rem;">
                Select a video file (MP4, AVI, MOV) to analyze waste frame by frame
            </p>
        </div>
    """, unsafe_allow_html=True)

    uploaded_video = st.file_uploader(
        "Choose a video file",
        type=["mp4", "avi", "mov"],
        help="Upload a video for waste detection"
    )

    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        video_path = tfile.name

        cap = cv2.VideoCapture(video_path)
        frame_area = st.empty()
        progress = st.progress(0)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (640, int(640 * 9 / 16)))
            results = model.predict(frame, conf=0.4)
            detected = set(model.names[int(c)] for r in results for c in r.boxes.cls) if results else set()
            r, nr, h, o, b = classify_items(detected)
            annotated = results[0].plot() if results else frame

            frame_area.image(annotated, channels="BGR")
            show_sidebar_results(r, nr, h, o, b, detected)

            current_frame += 1
            progress.progress(min(current_frame / total_frames, 1.0))

        cap.release()
        st.success("✅ Video analysis complete!")




    # Webcam Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #2196F3; margin-top: 0;">📷 Live Camera Detection</h2>
            <p style="color: #666; margin-bottom: 1rem;">
                Use your camera for real-time waste detection and classification
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Webcam Control Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        start = st.button("▶️ Start Camera", key="start", use_container_width=True,
                         help="Begin live camera detection")
    with col2:
        stop = st.button("⏹️ Stop Camera", key="stop", use_container_width=True,
                        help="Stop camera but keep last frame")
    with col3:
        cancel = st.button("❌ Clear All", key="cancel", use_container_width=True,
                          help="Stop camera and clear all results")

    # Camera Feed Area
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 1.5rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h3 style="color: #333; margin-top: 0;">📺 Camera Feed</h3>
        </div>
    """, unsafe_allow_html=True)

    frame_area = st.empty()

    if start:
        st.session_state.webcam_on = True

    if stop:
        st.session_state.webcam_on = False

    if cancel:
        st.session_state.webcam_on = False
        st.session_state.last_frame = None
        st.session_state.detected_r.clear()
        st.session_state.detected_nr.clear()
        st.session_state.detected_h.clear()
        st.session_state.detected_o.clear()
        st.session_state.detected_b.clear()
        st.session_state.detected_all.clear()


    if st.session_state.webcam_on:
        cap = cv2.VideoCapture(settings.WEBCAM_PATH)
        while st.session_state.webcam_on:
            ret, frame = cap.read()
            if not ret:
                st.warning("Could not access webcam.")
                break
            frame = cv2.resize(frame, (640, int(640 * 9 / 16)))
            results = model.predict(frame, conf=0.4)
            detected = set(model.names[int(c)] for r in results for c in r.boxes.cls) if results else set()
            r, nr, h, o, b = classify_items(detected)

            annotated = results[0].plot() if results else frame
            frame_area.image(annotated, channels="BGR")

            st.session_state.last_frame = annotated
            st.session_state.detected_r = r
            st.session_state.detected_nr = nr
            st.session_state.detected_h = h
            st.session_state.detected_o = o
            st.session_state.detected_b = b
            st.session_state.detected_all = detected

            show_sidebar_results(r, nr, h, o, b, detected)

        cap.release()

    elif st.session_state.last_frame is not None:
        frame_area.image(st.session_state.last_frame, channels="BGR")
        show_sidebar_results(
            st.session_state.detected_r,
            st.session_state.detected_nr,
            st.session_state.detected_h,
            st.session_state.detected_o,
            st.session_state.detected_b,
            st.session_state.detected_all,
        )
    else:
        frame_area.empty()

    # Footer
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   color: white; padding: 1.5rem; border-radius: 15px; text-align: center;
                   margin-top: 3rem;">
            <h3 style="margin: 0;">🌱 EcoDetect AI</h3>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">
                Making waste management smarter with artificial intelligence
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Instructions and Tips
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-top: 2rem;">
            <h3 style="color: #4CAF50; margin-top: 0;">💡 Tips for Better Detection</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                       gap: 1rem; margin-top: 1rem;">
                <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px;">
                    <strong>📸 Good Lighting</strong><br>
                    <span style="color: #666;">Ensure adequate lighting for clear images</span>
                </div>
                <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px;">
                    <strong>🎯 Clear Focus</strong><br>
                    <span style="color: #666;">Keep waste items in focus and visible</span>
                </div>
                <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px;">
                    <strong>📏 Proper Distance</strong><br>
                    <span style="color: #666;">Maintain appropriate distance from objects</span>
                </div>
                <div style="background: #fff3e0; padding: 1rem; border-radius: 8px;">
                    <strong>🧹 Clean Background</strong><br>
                    <span style="color: #666;">Use clean backgrounds for better accuracy</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Optional: enable direct run of app.py
if __name__ == "__main__":
    run_app()
