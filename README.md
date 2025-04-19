# Not Hot Dog Snowflake 🍽️

![1_VrpXE1hE4rO1roK0laOd7g](https://github.com/user-attachments/assets/44be7c32-398f-47aa-97f4-32d0c39f123b)


A modern reimagining of the iconic "Not Hotdog" app from HBO's *Silicon Valley*, rebuilt entirely within the Snowflake ecosystem. This application leverages Snowflake's **Cortex Complete Multimodal** capabilities and **Streamlit in Snowflake (SiS)** to classify images as "hot dog" or "not hot dog" directly within your data warehouse—no external services required

---

## 🔍 Features

- **Image Classification** Upload an image to determine if it depicts a hot dog.
- **Snowflake Cortex Integration** Utilizes Snowflake's Cortex Complete Multimodal functions for image analysis
- **Streamlit in Snowflake** Interactive user interface built with Streamlit, running natively within Snowflake
- **Serverless Deployment** No need for external servers or infrastructure; everything operates within Snowflake

---

## 🚀 Getting Started

### Prerequisites
- An active Snowflake account with access o:
 - **Cortex Complete Multimodal** functions
 - **Streamlit in Snowflake**


### Setup Instructions

1. **Set Up the Database Objects**:

  - Open a new worksheet in Snowsigt.
  - Execute the SQL commands found in `app.sql` to create necessary tables and stages

2. **Create a New Streamlit App in Snowflake**:

  - Navigate to the **Streamlit** section in Snowsight.
  - Click on **+ Streamlit** to create a new application
  - Copy the contents of `app.py` into the Streamlit editor

3. **Run the Application**:

  - Return to your Streamlit app in Snowsight
  - Click **Run** to launch the application
  - Upload an image and see the classification result

---

## 📁 Project Structue

```plaintext
not-hot-dog-snowflake/
├── app.py       # Streamlit application code
├── app.sql      # SQL scripts for setting up database objects
└── README.md    # Project documentation
```

## 🧠 Technical Details

### Cortex Complete Multimodal

Snowflake's fully managed AI service that enables multimodal data analysis, allowing for seamless integration of image and text data processing within SQL and Python environments.

### Streamlit in Snowflake (SS)

Allows developers to build and deploy Streamlit applications directly within the Snowflake platform, facilitating interactive data applications without the need for external hosting.

---

## 🎬 Inspiration

This project draws inspiration from the fictional "Not Hotdog" app featured in HBO's *Silicon Valley*, where the app humorously identifies whether a given image is a hot dog or not. The original concept has been reimagined using modern data tools to demonstrate the capabilities of Snowflake's AI and application development feaures.

---

