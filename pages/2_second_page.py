import streamlit as st

# With the help of AI:

def show_about_page():
    st.markdown("""
    # CSV File Analyst: Interactive Data Analytics Web App

    An interactive, web-based data analysis tool built with Python, Streamlit, and Matplotlib. This application allows users to dynamically upload any e-commerce or retail dataset in CSV format, analyze its structure, perform multi-level filtering, and generate real-time data visualizations.

    ### 🚀 Features
    * **Dynamic File Uploading:** Supports any user-provided CSV file.
    * **Instant Dataset Overview:** Automatically displays the total number of rows and columns upon upload.
    * **Multi-Criteria Advanced Filtering:** * Categorical filtering via drop-down select boxes (`City`, `Product Type`, `Customer Gender`).
      * Numerical range filtering using a dual-ended interactive `Slider` (`Price`).  
      * Conditional filtering using a `Checkbox` to instantly isolate specific states (e.g., returned orders).

    * **Responsive Visualizations:** * A **Histogram** showing the price distribution of the filtered subset.
      * A **Bar Chart** aggregating the total sales amount by product categories.  
      * *Smart Error Handling:* Built-in guards prevent app crashes and display warning messages if selected filters yield an empty dataset.

    ### 🛠️ Tech Stack
    * **Frontend/Framework:** Streamlit
    * **Data Manipulation:** Pandas
    * **Data Visualization:** Matplotlib
    """)


# Если этот файл запускается напрямую
if __name__ == "__main__":
    show_about_page()