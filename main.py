import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Options for length, language, and tone
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Formal", "Casual"]  # Added tone options

# Main app layout
def main():
    st.subheader("PostForge: LinkedIn Post Generator")

    # Create four columns for the dropdowns (Topic, Length, Language, Tone)
    col1, col2, col3, col4 = st.columns(4)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("Language", options=language_options)

    with col4:
        # Dropdown for Tone (Formal or Casual)
        selected_tone = st.selectbox("Tone", options=tone_options)

    # Generate Button
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag, selected_tone)  # Pass tone
        st.write(post)


# Run the app
if __name__ == "__main__":
    main()
