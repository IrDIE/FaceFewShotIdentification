import streamlit as st

from streamlit_webrtc import webrtc_streamer

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