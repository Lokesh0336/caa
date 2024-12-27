import streamlit as st

# Define a function to evaluate the calculator input
def evaluate_expression(expression):
    try:
        # Replace multiplication and division symbols for Python's eval function
        expression = expression.replace("×", "*").replace("÷", "/")
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# Main Streamlit app
def main():
    st.set_page_config(page_title="iPhone-like Calculator", layout="centered")
    st.title("📱 Modern Calculator")

    # Initialize session state for the input
    if "input" not in st.session_state:
        st.session_state.input = ""

    # Display the input
    st.markdown(
        f"""
        <div style="background-color:#1C1C1E; color:white; font-size:40px; text-align:right; padding:20px; border-radius:8px;">
            {st.session_state.input if st.session_state.input else "0"}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Buttons for the calculator
    buttons = [
        ["C", "±", "%", "÷"],
        ["7", "8", "9", "×"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "="],
    ]

    # Create button layout
    for row in buttons:
        cols = st.columns(len(row))
        for i, btn in enumerate(row):
            with cols[i]:
                if st.button(btn, use_container_width=True, key=f"btn_{btn}"):
                    handle_button_click(btn)

# Handle button click
def handle_button_click(btn):
    if btn == "C":
        st.session_state.input = ""
    elif btn == "±":
        try:
            if st.session_state.input.startswith("-"):
                st.session_state.input = st.session_state.input[1:]
            else:
                st.session_state.input = "-" + st.session_state.input
        except:
            st.session_state.input = ""
    elif btn == "%":
        try:
            st.session_state.input = str(float(st.session_state.input) / 100)
        except:
            st.session_state.input = ""
    elif btn == "=":
        st.session_state.input = evaluate_expression(st.session_state.input)
    else:
        st.session_state.input += btn

# Run the app
if __name__ == "__main__":
    main()
