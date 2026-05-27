import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Please upload a file in CSV format",
                 type=["csv"],
            )
if uploaded_file:
    st.subheader("Loaded data")
    df = pd.read_csv(uploaded_file)
    st.text(f"Number of rows: {df.shape[0]}")
    st.text(f"Number of columns: {df.shape[1]}")

    city = st.selectbox("Choose city", df.city.unique())
    product_type = st.selectbox("Choose product type", df.category.unique())
    gender = st.selectbox("Choose gender", df.customer_gender.unique())

    min_price = float(df.price.min())
    max_price = float(df.price.max())

    price_range = st.slider(
        "Select price range",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )

    show_only_returned = st.checkbox("Show only returned order lines")

    filtered = df[
        (df.city == city) &
        (df.category == product_type) &
        (df.customer_gender == gender) &
        (df.price >= price_range[0]) &
        (df.price <= price_range[1])
        ]

    if show_only_returned:
        filtered = filtered[filtered.returned == True]

    st.dataframe(filtered)

    if not filtered.empty: # with help of AI
       fig, ax = plt.subplots()

       ax.hist(filtered['price'],bins=15, color='skyblue', edgecolor='black')
       ax.set_title('Distribution of Prices for Filtered Data')
       ax.set_xlabel('Price')
       ax.set_ylabel('Number of Items (Frequency)')
       st.pyplot(fig)

    else:
        st.warning("No data available for the selected filters to build a histogram.") # with help of AI

    if not filtered.empty:
        category_sales = filtered.groupby('category')['price'].sum().sort_values(ascending=False)

        fig2, ax2 = plt.subplots()

        ax2.bar(category_sales.index, category_sales.values, color='lightgreen', edgecolor='black')
        ax2.set_title('Sales Amount by Product Categories')
        ax2.set_xlabel('Category')
        ax2.set_ylabel('Total Sales')

        st.pyplot(fig2)

    else:
        st.warning("No data available to build a bar chart.")


