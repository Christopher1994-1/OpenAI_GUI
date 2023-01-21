import os
import openai
import json
import customtkinter
from tkinter import *
import time
import threading


class App:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.something = 0
        self.root.title("Open API Chat")
        self.root.iconbitmap("darkModeV.ico")
        self.root.geometry("410x300") # L x H change back to 270 or 280?
        self.root.config(background="#282828")
        
        
        # ------------ First Frame ------------ #
        self.first_frame = customtkinter.CTkFrame(self.root, fg_color='#282828', border_color=("black"), width=300)
        self.first_frame.pack(pady=(0, 20))#side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        # Creating a string variable to hold the user input
        self.input = customtkinter.StringVar(value="Enter Your Input Below...")
        # Creating a input label to show the string variable
        self.input_label = customtkinter.CTkLabel(self.first_frame, textvariable=self.input, width=300)
        self.input_label.pack()
        
        
        # Creating a string variable to hold the user input
        self.ai = customtkinter.StringVar(value="")
        # Creating an input label to show the string variable
        self.ai_label = customtkinter.CTkLabel(self.first_frame, textvariable=self.ai, wraplength=300)
        self.ai_label.pack()
        
        
        

        
        
        # ------------ Second Frame ------------ #
        self.second_frame = customtkinter.CTkFrame(self.root, fg_color='#282828', border_color=("black"))
        self.second_frame.pack(side=BOTTOM, pady=(0, 10))#side=TOP, anchor="w", padx=(10, 0), pady=(15, 0))
        
        
        # Creating a entry box for user input
        self.entry = customtkinter.CTkEntry(master=self.second_frame, placeholder_text="Enter Text", width=250, height=32, border_width=2, corner_radius=10)
        self.entry.grid(row=0, column=0)
        
        
        # Creating a button with the text "Enter", which when clicked calls the enter_btn method
        self.button = customtkinter.CTkButton(master=self.second_frame, corner_radius=8, text="Enter", width=30, height=32, command=lambda: self.enter_btn("3"))
        self.button.grid(row=0, column=1, padx=(5, 0))
        # Also bound to the '<Return>' or enter key for the same action
        self.root.bind("<Return>", lambda e: self.enter_btn('0'))
        
        
        # Creating a button with the text "Clear", which when clicked calls the clear_btn method
        self.button = customtkinter.CTkButton(master=self.second_frame, corner_radius=8, text="Clear", width=30, height=32, command=lambda: self.clear_btn("3"))
        self.button.grid(row=0, column=2, padx=(5, 0))
        # Also bound to the 'c' key for the same action
        self.root.bind("<Control-c>", lambda e: self.clear_btn("c"))
        
        


    
        self.root.mainloop()
        
        
        
        
    # All App Class Methods ****
                
                
                
    # Enter Button Method
    def enter_btn(self, f):
        """
        Method that is called when the enter button is clicked in the GUI.
        
        Parameters:
            f (function): The function to be called when the button is clicked.
        
        Returns:
            None
            
        """
        # StrVariable that is set
        entry_value = self.entry.get()
        
        
        user_input = self.input.get()
        
        self.input_list = []
        
        
        if entry_value == "" and user_input != '':
            self.input.set(value="Please Enter a Prompt")

        elif user_input != "" and entry_value != '':
            self.input.set(value="Loading...")
            self.input_list.append(entry_value)
            self.entry.delete(0, END)
            threading.Thread(target=self.get_response, args=(entry_value,)).start()


    
    # Second Ai Response
    def get_response(self, entry_value):
        """
        Method that gets the response from the AI model using the OpenAI API.
        
        Parameters:
            entry_value (str): The text prompt that the API will use as the starting point for generating a response.
        
        Returns:
            None
            
        """
        start_time = time.time()
                
            
        user_input = self.input.get()
        entry_value = self.input_list[0]
        
        # TODO we need to delete the entry box after hitting the box but then when this method is called
        # it messes things up
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 2:
                # code to execute when 2 seconds have passed
                response = self.api_response(entry_value)
                self.input.set(value=entry_value)
                self.ai.set(value=response)
                del self.input_list[0]
                break

    
    
    # Clear Button Method
    def clear_btn(self, f):
        """
        Method that clears the input and output fields in the GUI.
        
        Parameters:
            f (function): The function to be called when the button is clicked.
        
        Returns:
            None
            
        """
        value = self.input.get()
        entry_value = self.entry.get()
        
        if entry_value == '':
            self.input.set('Please Enter Your Input Below')
        else:
            self.input.set('Please Enter Your Input Below')
            self.ai.set("")
            
        
    
    # AI API Response Method
    def api_response(self, prompt):
        """
        Generates a text response based on a given prompt using the OpenAI API.
        
        Parameters:
            prompt (str): The text prompt that the API will use as the starting point for generating a response.
        
        Returns:
            str: The generated text response.
            
        Example:
            response = api_response("What is the weather like today?")
            print(response)
            # Output: "The weather today is sunny with a high of 75 degrees."
        """
        openai.api_key = "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"
        # openai.api_key = os.environ("OpenAI_Key")


        model_response = str(openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.9
        ))
        json_obj = json.loads(model_response)
        response = json_obj["choices"][0]["text"]
        return response


    
    

app = App()