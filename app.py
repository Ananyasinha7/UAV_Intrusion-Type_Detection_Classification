import streamlit as st
import numpy as np
import pickle

with open('bestmodel.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('Label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

features = [
    'timestamp_c', 'frame.number', 'frame.len', 'wlan.ta', 'wlan.sa', 'wlan.ra',
    'wlan.da', 'wlan.bssid', 'wlan.duration', 'wlan.frag', 'wlan.seq',
    'wlan.fc.type', 'wlan.fc.subtype', 'data.len', 'tcp.hdr_len', 'llc.type',
    'data.data', 'tcp.window_size', 'udp.length', 'tcp.options', 'ip.hdr_len',
    'ip.src', 'ip.id', 'frame.protocols', 'ip.flags', 'tcp.flags', 'ip.dst',
    'tcp.srcport', 'ip.len', 'tcp.ack_raw', 'udp.srcport', 'ip.ttl',
    'tcp.dstport', 'udp.dstport', 'time_since_last_packet', 'ip.proto', 'tcp.seq_raw'
]

st.title(" UAV Intrusion Type Detection")

st.markdown("""
###  Enter all 37 feature values (comma-separated):
Paste your values in the exact order below:

`timestamp_c, frame.number, frame.len, wlan.ta, wlan.sa, wlan.ra, wlan.da, wlan.bssid, wlan.duration, wlan.frag, wlan.seq, wlan.fc.type, wlan.fc.subtype, data.len, tcp.hdr_len, llc.type, data.data, tcp.window_size, udp.length, tcp.options, ip.hdr_len, ip.src, ip.id, frame.protocols, ip.flags, tcp.flags, ip.dst, tcp.srcport, ip.len, tcp.ack_raw, udp.srcport, ip.ttl, tcp.dstport, udp.dstport, time_since_last_packet, ip.proto, tcp.seq_raw`
""")

csv_input = st.text_area("Enter comma-separated values here:")

if st.button("Predict Intrusion Type"):
    try:
        input_list = [float(i.strip()) for i in csv_input.split(',')]

        if len(input_list) != 37:
            st.error(" Please enter exactly 37 comma-separated values.")
        else:
            input_array = np.array([input_list])
            scaled_input = scaler.transform(input_array)

            prediction = model.predict(scaled_input)[0]
            probability = model.predict_proba(scaled_input)[0]

            predicted_label = le.inverse_transform([prediction])[0]

            st.success(f" Predicted UAV Intrusion Class: **{predicted_label}**")
            st.write("Prediction Probabilities:")
            st.json({f"Class {le.inverse_transform([i])[0]}": float(prob) for i, prob in enumerate(probability)})

    except Exception as e:
        st.error(f"⚠️ Error processing input: {e}")
