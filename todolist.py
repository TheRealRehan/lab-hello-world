import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

new_task = st.text_input("Add a new task:")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task.strip())
        st.experimental_rerun()  

st.subheader("Your Tasks")
updated_tasks = []

for task in st.session_state.tasks:
   
    delete = st.checkbox(task, key=task)
    if not delete:
        updated_tasks.append(task)

if updated_tasks != st.session_state.tasks:
    st.session_state.tasks = updated_tasks
    st.experimental_rerun()  







