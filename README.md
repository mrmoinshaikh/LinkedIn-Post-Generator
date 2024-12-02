# PostFroge: LinkedIn Post Generator

PostForge is a powerful LinkedIn post generation tool built using Llama 3, an advanced language model that powers the generation of engaging and thought-provoking posts. This tool allows users to create impactful LinkedIn posts by leveraging AI.

## The Appearance of the Generator

Here’s an example of how the generated post might look:

![Post Example](images/Screenshot%202024-12-02%20185255.png)


## Features
- Automatically generate LinkedIn posts based on provided input.
- Customizable tone and style for posts.
- Simple command-line interface for generating posts.
- Easy to extend for other social media platforms.

## The Example of the Generated Post

Here’s an example of how the generated post might look:

![Post Example](images/Screenshot%202024-12-02%20185510.png)

Tech Stack
Python: The primary language used for backend development.
Llama 3: The core language model used for post generation.
Streamlit: A framework used to build the interactive web interface.
Groq Cloud: A cloud platform for fast and scalable AI model deployment and inference.
Other Libraries: pandas, NumPy, etc. (if applicable)
Setup
Prerequisites
Ensure you have the following dependencies installed:

Python 3.x
Llama 3 model (or relevant dependency for the model)
Streamlit and other necessary Python libraries.
Groq Cloud account and API credentials for model inference.
Steps to Set Up Locally
Clone the repository to your local machine.

bash
Copy code
git clone https://github.com/yourusername/PostForge.git
cd PostForge
Set up your environment variables by editing the .env file or setting them in your system. Ensure you have the Groq Cloud API key in the .env file or as an environment variable for authentication.

Install the required Python packages:

 ```commandline
     pip install -r requirements.txt
    ```

```commandline
   streamlit run main.py
   ```
Once the app is running, it will open in your default web browser, and you can interact with the LinkedIn post generator via the UI.

Usage
After setting up the project, you can use the generator by running the main.py script. You can customize how the posts are generated by modifying the input or tweaking the parameters.

Contributing

If you’d like to contribute to the development of PostFroge, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!

Acknowledgements

Inspired by the [Codebasics GitHub](https://github.com/codebasics) YouTube Channel  for the knowledge and implementation strategies used.
