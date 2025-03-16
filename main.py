import streamlit as st

st.sidebar.title("🔧 Password Tips")
st.sidebar.write("✅ Minimum 8 characters")
st.sidebar.write("✅ At least one uppercase letter")
st.sidebar.write("✅ At least one lowercase letter")
st.sidebar.write("✅ At least one digit")
st.sidebar.write("✅ At least one special character (!@#$%^&*)")
st.sidebar.title("🔒 Note:")
st.sidebar.info("Your password is never stored or transmitted.")

st.title("🔒 Password Strength Meter!")
st.write("Enter your password to check its strength.")
password = st.text_input("Password", type="password")

score = 0
feedback = []

if st.button("Check Strength"):
    if len(password) < 8:
        feedback.append("❌ Password is too short. It should be at least 8 characters.")
    else:
        score += 1
    if not any(char.isupper() for char in password):
        feedback.append("❌ Password should have at least one uppercase letter.")
    else:
        score += 1
    if not any(char.islower() for char in password):
        feedback.append("❌ Password should have at least one lowercase letter.")
    else:
        score += 1
    if not any(char.isdigit() for char in password):
        feedback.append("❌ Password should have at least one digit.")
    else:
        score += 1    
    if not any(char in "!@#$%^&*()_+-=" for char in password):
        feedback.append("❌ Password should have at least one special character.")
    else:
        score += 1
    if feedback:
        for tip in feedback:
            st.error(tip)  
else:
    feedback.append("✅ Password meets all the criteria")



if score == 5:
    st.success("✅ Very strong password. Excellent!")
elif score == 4:
     st.success("✅ Strong password. Good job!")
elif score == 3:
    st.warning("⚠️ Medium Strength password. Try to make it stronger!")
elif score == 2:
    st.warning("⚠️ Weak password. Could be cracked easily!")
else:
    st.error("Very weak password. Easily cracked!")




