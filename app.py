# Sovereign Identity
st.set_page_config(page_title="Sovereign Audit 325270269318", page_icon="⚖️")

st.title("⚖️ Sovereign Logic Analyzer")
st.subheader("Master ID: 325270269318")

st.markdown("---")
st.write("अपनी बिजली के बिल का 'Surgical Audit' करें।")

# User Input Sections
col1, col2 = st.columns(2)
with col1:
    units = st.number_input("कुल यूनिट (Units):", min_value=0.0, value=2300.0)
    load = st.number_input("सक्षम लोड (Load in KW):", min_value=0.1, value=1.0)
with col2:
    days = st.number_input("बिल के दिन (Days):", min_value=1, value=88)
    mdi = st.number_input("Max Demand (MDI):", min_value=0.0, value=1.2)

# The Surgical Logic Engine
if st.button("Start Surgical Audit"):
    max_possible = load * 24 * days
    st.markdown("### 📊 Analysis Report")
    
    if units > max_possible:
        leakage = units - max_possible
        divergence = (leakage / max_possible) * 100
        st.error(f"🚨 FRAUD DETECTED!")
        st.warning(f"1KW के लोड पर {days} दिन में अधिकतम {max_possible} यूनिट ही मुमकिन हैं।")
        st.info(f"Ghost Units Detected: {leakage} Units ({divergence:.2f}% Error)")
    else:
        st.success("✅ डेटा लॉजिकल है।")
        
    if mdi > load:
        st.warning(f"⚠️ MDI Breach: रउआर लोड {load}KW बा लेकिन डिमांड {mdi}KW बा। पेनल्टी लग सकत बा।")

st.markdown("---")
st.caption("© 2026 Sovereign Audit System | 325270269318")
