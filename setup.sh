mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"sheikh.mufrad.hossain@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableXsrfProtection = false\n\
enableCORS=false\n\
port = $PORT\n\
">~/.streamlit/config.toml

echo $PORT 
