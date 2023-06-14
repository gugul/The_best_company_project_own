import streamlit
import pandas

streamlit.set_page_config(layout="wide")

streamlit.header("The Best Company")
streamlit.write("""
Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae 
dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam 
est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam 
eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim 
ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid 
ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, 
quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?"
                """)
streamlit.subheader("Our Team")

col1, col2, col3 = streamlit.columns(3)

data_file = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in data_file[:4].iterrows():
        streamlit.header(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        streamlit.write(row["role"])
        streamlit.image("images/" + row["image"])


with col2:
    for index, row in data_file[4:8].iterrows():
        streamlit.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        streamlit.write(row["role"])
        streamlit.image("images/" + row["image"])


with col3:
    for index, row in data_file[8:12].iterrows():
        streamlit.header(row["first name"].capitalize() + " " + row["last name"].capitalize())
        streamlit.write(row["role"])
        streamlit.image("images/" + row["image"])





