import streamlit as st

# Single tab for Stock Valuation using Benjamin Graham Valuation Equation
st.title("Stock Valuation")

# Inputs for Benjamin Graham Valuation
earnings_per_share = st.number_input("Enter Earnings per Share (EPS)", value=5.0)
growth_rate_eps = st.number_input("Enter estimated growth rate for EPS (as a percentage)", 0.0, 100.0, 5.0)
discount_rate = st.number_input("Enter discount rate (as a percentage)", 0.0, 100.0, 4.5)

# Benjamin Graham Valuation Equation Calculation
graham_stock_price = (earnings_per_share * (8.5 + 2 * growth_rate_eps)) * 4.4 / discount_rate

# Display the result in a larger font with light blue background, rounded edges
st.write(f"""
    <div style='text-align: center; background-color: #d9edf7; padding: 15px; 
                border-radius: 10px; font-size: 24px; color: #31708f;'>
        Estimated stock price using Benjamin Graham Valuation: <strong>${graham_stock_price:.2f}</strong>
    </div>
""", unsafe_allow_html=True)

# LaTeX for Benjamin Graham Valuation Equation
st.latex(r'''
\text{Benjamin Graham Valuation Equation:} \ P = \frac{E \times (8.5 + 2 \times g_{\text{EPS}}) \times 4.4}{r}
''')

# Bullet points explaining the variables in the formula
st.markdown("""
**Where:**
- **P** = Price
- **E** = Earnings per Share (EPS)
- **g** = Growth Rate of EPS
- **r** = Discount Rate
""")
