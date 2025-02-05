from langchain_openai import ChatOpenAI

# Initialize the model with your API key
llm = ChatOpenAI(model="gpt-4o-mini", api_key=process.env.API_KEY)

# Read the content from hi.txt
with open('output.txt', 'r') as file:
    input_text = file.read()

# Invoke the model with the read content
response = llm.invoke(input_text)

# Overwrite response.txt with the response content
with open('views/response.ejs', 'w') as response_file:
    response_file.write(response.content)