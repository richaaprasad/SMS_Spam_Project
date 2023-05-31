# Code to create directories

mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $port\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/credentials.toml