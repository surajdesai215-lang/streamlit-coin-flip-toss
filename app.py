import streamlit as st
import random

st.title("🪙 Coin Toss toss")
st.subheader("if you dont have a coin for toss use me ")

st.write("Choose Heads or Tails and toss the coin!")

choice = st.radio(
    "Select your choice:",
    ["Heads", "Tails"]
)

if st.button("Toss Coin"):
    result = random.choice(["Heads", "Tails"])

    st.subheader(f"Coin Result: {result}")

    if choice == result:
        st.success("🎉 Congratulations! You Won!")
    else:
        st.error("😔 Better Luck Next Time!")