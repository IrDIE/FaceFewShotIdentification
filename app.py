import streamlit as st
from streamlit_webrtc import webrtc_streamer
from camera_input_live import camera_input_live
import cv2
import numpy as np

c = webrtc_streamer(key="example2"
                    , rtc_configuration=
                    {
                        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                        #     [
                        #     {
                        #         "urls": ["stun:fr-turn2.xirsys.com"]
                        #     }, {
                        #         "username": "PhUZzBq2wugeeSwzRxiwKCluHmp2OrZVfKvSWUMKVKJNK8B08EiCqVacNkLcfxkvAAAAAGTMeP1JcmluYQ==",
                        #         "credential": "1f5dbe1c-327c-11ee-a998-0242ac120004",
                        #         "urls": [
                        #             "turn:fr-turn2.xirsys.com:80?transport=udp",
                        #             "turn:fr-turn2.xirsys.com:3478?transport=udp",
                        #             "turn:fr-turn2.xirsys.com:80?transport=tcp",
                        #             "turn:fr-turn2.xirsys.com:3478?transport=tcp",
                        #             "turns:fr-turn2.xirsys.com:443?transport=tcp",
                        #             "turns:fr-turn2.xirsys.com:5349?transport=tcp"
                        #         ]}
                        #
                        # ]
                    },
                    media_stream_constraints={"video": True, "audio": False},

                    )

st.button("Add person")

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))



image = camera_input_live()

if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)

    if data:
        st.write("# Found QR code")
        st.write(data)
        with st.expander("Show details"):
            st.write("BBox:", bbox)
            st.write("Straight QR code:", straight_qrcode)