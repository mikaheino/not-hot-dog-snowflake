Not Hot Dog Snowflake
A modern reimagining of the iconic "Not Hotdog" app from HBO's Silicon Valley, rebuilt entirely within the Snowflake ecosystem. This application leverages Snowflake's Cortex Complete Multimodal capabilities and Streamlit in Snowflake (SiS) to classify images as "hot dog" or "not hot dog" directly within your data warehouse—no external services required.​
Paperspace by DigitalOcean Blog
+4
Product Hunt
+4
Engadget
+4
DEV Community

🔍 Features
Image Classification: Upload an image to determine if it depicts a hot dog.

Snowflake Cortex Integration: Utilizes Snowflake's Cortex Complete Multimodal functions for image analysis.

Streamlit in Snowflake: Interactive user interface built with Streamlit, running natively within Snowflake.

Serverless Deployment: No need for external servers or infrastructure; everything operates within Snowflake.​
Product Hunt
+1
Engadget
+1
DEV Community

🚀 Getting Started
Prerequisites
An active Snowflake account with access to:

Cortex Complete Multimodal functions

Streamlit in Snowflake (SiS)

Python 3.11 or later

Installed packages:

snowflake-ml-python (version 1.7.4 or later)

streamlit​
Streamlit Docs
+2
DEV Community
+2
Snowflake Quickstarts
+2
DEV Community
+4
Medium
+4
Snowflake Quickstarts
+4
Reddit
+1
Snowflake Quickstarts
+1
DEV Community
+1
DEV Community
+1

Setup Instructions
Clone the Repository:

bash
Kopioi
Muokkaa
git clone https://github.com/mikaheino/not-hot-dog-snowflake.git
cd not-hot-dog-snowflake
Create a New Streamlit App in Snowflake:

Navigate to the Streamlit section in Snowsight.

Click on + Streamlit to create a new application.

Copy the contents of app.py into the Streamlit editor.​
snowflake.com
+7
DEV Community
+7
DEV Community
+7
DEV Community
+1
DEV Community
+1

Set Up the Database Objects:

Open a new worksheet in Snowsight.

Execute the SQL commands found in app.sql to create necessary tables and stages.​
Snowflake Quickstarts

Run the Application:

Return to your Streamlit app in Snowsight.

Click Run to launch the application.

Upload an image and see the classification result.​
Medium
snowflake.com
+3
Paperspace by DigitalOcean Blog
+3
Medium
+3

📁 Project Structure
plaintext
Kopioi
Muokkaa
not-hot-dog-snowflake/
├── app.py       # Streamlit application code
├── app.sql      # SQL scripts for setting up database objects
└── README.md    # Project documentation
🧠 Technical Details
Cortex Complete Multimodal: Snowflake's fully managed AI service that enables multimodal data analysis, allowing for seamless integration of image and text data processing within SQL and Python environments. ​
Snowflake Quickstarts

Streamlit in Snowflake (SiS): Allows developers to build and deploy Streamlit applications directly within the Snowflake platform, facilitating interactive data applications without the need for external hosting. ​
Medium

🎬 Inspiration
This project draws inspiration from the fictional "Not Hotdog" app featured in HBO's Silicon Valley, where the app humorously identifies whether a given image is a hot dog or not. The original concept has been reimagined using modern data tools to demonstrate the capabilities of Snowflake's AI and application development features. ​
Product Hunt
+4
The Verge
+4
Paperspace by DigitalOcean Blog
+4

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.​

