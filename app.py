import streamlit as st
from streamlit_webrtc import webrtc_streamer
import dlib
import cv2
import numpy as np



def face_points_callback(frame):
    frame = frame.to_ndarray(format="bgr24")
    predictor_path = './pretrained_models/shape_predictor_68_face_landmarks.dat'
    predictor = dlib.shape_predictor(predictor_path)
    img_shape = frame.shape
    points_face = []

    det = dlib.rectangle(left=0, top=0, right=img_shape[1], bottom=img_shape[0])
    shape = predictor(frame, det)
    for i in range(68):
        point_x, point_y  = shape.part(i).x, shape.part(i).y
        points_face.append([point_x, point_y])


    for i, point in enumerate(points_face):
        point = list(map(int, point))
        color = (227, 68, 100)
        if i == 30:
            color = (0, 255, 0)
        frame = cv2.circle(frame, point, radius=2, color=color, thickness=-1)


webrtc_stream = webrtc_streamer(key="example2"
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
uploaded_image = st.file_uploader("Choose a image", accept_multiple_files=True)
if uploaded_image is not None:
    bytes_image = uploaded_image.getvalue()
    st.write(bytes_image)

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.write(type(bytes_data))

