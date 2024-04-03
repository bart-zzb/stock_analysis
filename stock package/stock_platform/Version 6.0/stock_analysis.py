# -*- coding: utf-8 -*-
#Version: Python 2
#------------------------------------------------------------------------
#                    Read CSV file of stock for analysis
#                         15th - Jan - 2021
#                            Author: Bart    
#------------------------------------------------------------------------

#reference: download csv file website: "www.stooq.com"

import os
import csv
import sys
from collections import OrderedDict
from datetime import datetime, timedelta
from decimal import getcontext, Decimal

#This is Pyside2 version
'''
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
'''

#This is PyQt5 version

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setObjectName("The_MainWindow")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stock Analysis")
        self.setGeometry(350, 80, 800, 600)
        
        self.first_widget = groupbox_4_for_FunctionPage("Selected File")
        self.first_widget.setMinimumWidth(780)
        self.second_widget = Tab()
        self.third_widget = main_progress_bar()

        #create the main button function
        self.second_widget.tab1.groupbox_3.process_button.pressed.connect(self.select_function)
        self.second_widget.tab1.groupbox_3.reset_button.pressed.connect(self.clear_selected_function)
        
        self.second_widget.tab2.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_data_from_date_function)

        self.second_widget.tab3.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_maximum_function)

        self.second_widget.tab4.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_week_value_function)
 
        self.second_widget.tab5.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_month_value_function)
        
        self.second_widget.tab6.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_year_value_function)

        self.second_widget.tab7.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.get_increase_rate_from_date_to_now_function)
        
        self.second_widget.tab8.groupbox_5_for_FunctionPage.pushbutton.pressed.connect(self.calculate_the_rate_from_two_dates_function)

        
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.first_widget)
        self.mainlayout.addWidget(self.second_widget)
        #self.mainlayout.addStretch()
        self.mainlayout.addWidget(self.third_widget)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.setSpacing(2)
        self.setLayout(self.mainlayout)

        #self.centralwidget.setLayout(self.mainlayout)
        '''
        #create the topwidget and topwidget_layout
        self.topwidget = QWidget()
        self.topwidget_layout = QVBoxLayout()
        self.topwidget_layout.addWidget(self.first_widget)
        self.topwidget_layout.addWidget(self.second_widget)
        self.topwidget_layout.setSpacing(0)
        self.topwidget_layout.setContentsMargins(10, 5, 10, 0)
        self.topwidget.setLayout(self.topwidget_layout)
        
        #create the centralwidget layout
        self.centralwidget = QWidget()
        self.centralwidget_layout = QVBoxLayout()
        self.centralwidget_layout.addWidget(self.topwidget)
        self.centralwidget_layout.addStretch()
        self.centralwidget_layout.addWidget(self.third_widget)
        self.centralwidget_layout.setSpacing(0)
        self.centralwidget_layout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setLayout(self.centralwidget_layout)

        '''

    #create all the function
    def read_csv_and_run_function(self):
        selected_filename = self.first_widget.widget_list
        filepath = self.first_widget.filepath
        
        datadic = read_csv(filepath, selected_filename)

        return datadic

    def select_function(self):        
        file_selection = self.second_widget.tab1.groupbox_2.file_selection()
        
        #get the filepath and selected files
        self.filepath = self.second_widget.tab1.filepath
        self.selected_filename = []
        selected_filename_with_date = []
        for item in file_selection:
            self.selected_filename.append(item.text_1)
            selected_filename_with_date.append(item.text())

        #add the file to the tab widget layout
        self.first_widget.update_widget(self.filepath, self.selected_filename, selected_filename_with_date)

    def clear_selected_function(self):
        try:
            self.second_widget.tab1.groupbox_2.all_checkbox.setChecked(True)
            self.second_widget.tab1.groupbox_2.all_checkbox.setChecked(False)
            self.select_function()
        except Exception as e:
            pass

    def get_data_from_date_function(self):
        datadic = self.read_csv_and_run_function()
        
        total_value = 2+len(datadic)
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)
        
        new_date = self.second_widget.tab2.groupbox_5_for_FunctionPage.DateLineEdit_Calendar.date_input.text()
        temp_text = get_data_from_date(datadic, new_date, 1, self.third_widget)
        
        self.second_widget.tab2.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def get_maximum_function(self):
        datadic = self.read_csv_and_run_function()
        
        total_value = 2+len(datadic)
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)
        
        temp_text = get_maximum(datadic, 1, self.third_widget)   

        self.second_widget.tab3.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def get_week_value_function(self):
        datadic = self.read_csv_and_run_function()
        
        total_value = 2+len(datadic)*4
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)

        temp_text = get_week_value(datadic, 1, self.third_widget)

        self.second_widget.tab4.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def get_month_value_function(self):
        datadic = self.read_csv_and_run_function()
        
        total_value = 2+len(datadic)*4
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)

        temp_text = get_month_value(datadic, 1, self.third_widget)
        
        self.second_widget.tab5.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def get_year_value_function(self):
        datadic = self.read_csv_and_run_function()
        
        total_value = 2+len(datadic)*4
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)

        temp_text = get_year_value(datadic, 1, self.third_widget)
        
        self.second_widget.tab6.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def get_increase_rate_from_date_to_now_function(self):
        datadic = self.read_csv_and_run_function()
        users_date = self.second_widget.tab7.groupbox_5_for_FunctionPage.DateLineEdit_Calendar.date_input.text()
        
        total_value = 2+len(datadic)*2
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)

        temp_text = get_increase_rate_from_date_to_now(datadic, users_date, 1, self.third_widget)

        self.second_widget.tab7.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

    def calculate_the_rate_from_two_dates_function(self):
        datadic = self.read_csv_and_run_function()
        users_first_date = self.second_widget.tab8.groupbox_5_for_FunctionPage.DateLineEdit_Calendar_1.date_input.text()
        users_second_date = self.second_widget.tab8.groupbox_5_for_FunctionPage.DateLineEdit_Calendar_2.date_input.text()

        total_value = 2 + len(datadic)*2
        self.third_widget.setRange(0, total_value)
        self.third_widget.setValue(1)

        temp_text = get_increase_rate_from_the_two_date(datadic, users_first_date, users_second_date, 1, self.third_widget)

        self.second_widget.tab8.groupbox_6_for_FunctionPage.data.setText(temp_text)

        self.third_widget.setValue(total_value)

class Tab(QTabWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(780, 660)
        self.setStyleSheet(
            '''
               QTabWidget{
               background-color: #f1f1f1;
               }
            '''
            )

        #create seven tab widget
        self.tab1 = Tab_for_MainPage()
        
        #Create widget for the tabs
        self.tab2 = Tab_for_FunctionPage("Function 1: Search the data by the date",
                    "Please input the date you want to search: (format: 2007-02-15)", 1)

        self.tab3 = Tab_for_FunctionPage("Function 2: Search the maximum value for each stock", 
                    "Process Button", 0)

        self.tab4 = Tab_for_FunctionPage("Function 3: Search the value at the end of each week", 
                    "Process Button", 0)

        self.tab5 = Tab_for_FunctionPage("Function 4: Search the value at the end of each month", 
                    "Process Button", 0)

        self.tab6 = Tab_for_FunctionPage("Function 5: Search the value at the end of each year", 
                    "Process Button", 0)

        self.tab7 = Tab_for_FunctionPage("Function 6: Calculate the rate from Year to now", 
                    "Please input the Year you want to start: (format: 2007) (it will calucate from the first day of the year)", 1, int(1))

        self.tab8 = Tab_for_FunctionPage("Funciton 7: Calculate the rate from two dates you input",
                    "Please input the two dates: (format: 2007-02-15)", 2)

        #add all seven tabwidget
        self.addTab(self.tab1, "MainPage")
        self.addTab(self.tab2, "Date Rate")
        self.addTab(self.tab3, "Max-Min Value")
        self.addTab(self.tab4, "Week Rate")
        self.addTab(self.tab5, "Month Rate")
        self.addTab(self.tab6, "Year Rate")
        self.addTab(self.tab7, "Customize Rate(Year)")
        self.addTab(self.tab8, "Customize Rate(Day)")

class Tab_for_MainPage(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setObjectName("First_Tab")
        self.initUI()
        self.filepath = None

    def initUI(self):
        self.resize(800, 600)
        
        #create mainwindow contents
        self.groupbox_1 = groupbox_1_for_MainPage()
        self.groupbox_1.scan_button.pressed.connect(self.scan_button_function)
        #apply the qdialog button function to scan_function as well
        self.groupbox_1.file_path_widget.run_scan_button_function = self.scan_button_function

        self.groupbox_2 = groupbox_2_for_MainPage()

        self.groupbox_3 = groupbox_3_for_MainPage()
        
        #create the mainlayout
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.groupbox_1)
        self.mainlayout.addWidget(self.groupbox_2)
        self.mainlayout.addWidget(self.groupbox_3)
        self.mainlayout.setSpacing(8)
        self.mainlayout.addStretch()
        self.mainlayout.setContentsMargins(8, 15, 15, 8)

        self.setLayout(self.mainlayout)

    #Main Button function
    def scan_button_function(self):
        file_name = detect_csv(self.groupbox_1.file_path_widget.FilePath.text())[1]
        self.filepath = detect_csv(self.groupbox_1.file_path_widget.FilePath.text())[0]

        if file_name != []:
            self.groupbox_2.add_widget(file_name)
        else:
            self.groupbox_2.no_result()
        self.setLayout(self.mainlayout)

class Tab_for_FunctionPage(QWidget):
    def __init__(self, first_groupbox_title = "", second_groupbox_title = "", type_of_second_groupbox = 1, type_of_calendar = int(0)):
        super(self.__class__, self).__init__()
        self.first_groupbox_title = first_groupbox_title
        self.second_groupbox_title = second_groupbox_title
        self.type_of_second_groupbox = type_of_second_groupbox
        self.type_of_calendar = type_of_calendar
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        #create a qgroupbox for the file name
        self.file_label_groupbox = groupbox_4_for_FunctionPage(self.first_groupbox_title)
        
        #create a groupbox_5_for_FunctionPage
        self.groupbox_5_for_FunctionPage = groupbox_5_for_FunctionPage(self.second_groupbox_title, _type = self.type_of_second_groupbox, calendar_type = self.type_of_calendar)

        #create a scrollarea to show the data
        self.groupbox_6_for_FunctionPage = groupbox_6_for_FunctionPage()
        
        #create a layout, and add widget inside
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.file_label_groupbox)
        self.mainlayout.addWidget(self.groupbox_5_for_FunctionPage)
        self.mainlayout.addWidget(self.groupbox_6_for_FunctionPage)
        self.mainlayout.addStretch()
        self.mainlayout.setSpacing(8)
        self.mainlayout.setContentsMargins(15, 10, 15, 10)

        self.setLayout(self.mainlayout)

class groupbox_1_for_MainPage(QGroupBox):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.setTitle("Step 1: Please input the file folder dir: (it will scan all the csv files under the folder)")
        self.setMinimumHeight(60)
        self.setStyleSheet(
            '''
                QGroupBox
                {
                font:bold 14px;
                color:#000000;
                background-color: #f1f1f1;
                }
            '''
            )

        self.file_path_widget = file_path_widget()

        self.scan_button = Process_button("Scan")

        self.clear_button = Process_button("Clear")
        self.clear_button.pressed.connect(self.clear_button_function)

        self.mainlayout = QHBoxLayout()
        self.mainlayout.addWidget(self.file_path_widget)
        self.mainlayout.addWidget(self.scan_button)
        self.mainlayout.addWidget(self.clear_button)
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.mainlayout.addStretch()
        self.setLayout(self.mainlayout)

    def clear_button_function(self):
        self.file_path_widget.FilePath.setText("")

class groupbox_2_for_MainPage(QGroupBox):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()
        self.widget_list = []

    def initUI(self):
        self.setTitle("Step 2: Which files do you want to select:")
        self.setMinimumHeight(300)
        self.setStyleSheet(
            '''
                QGroupBox{
                font:bold 14px;
                color:#000000;
                background-color: #f1f1f1;
                }
            ''')
              
        #Create a widget which will be add into the QScrollArea later
        self.content_widget = QWidget()

        #Create a layout for the widget
        self.content_widget_layout = QVBoxLayout()
        self.content_widget_layout.setSpacing(0)
        self.content_widget_layout.setContentsMargins(30, 2, 30, 2)
        self.content_widget.setLayout(self.content_widget_layout)
        
        #Create the QScrollArea, set the content_widget inside
        self.scrollarea = QScrollArea()
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setWidget(self.content_widget)
        
        #Create the mainlayout of the QGroupbox, and add QScrollArea inside
        self.mainlayout = QVBoxLayout()        
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(15, 1, 15, 1)
        self.mainlayout.addWidget(self.scrollarea)
        self.setLayout(self.mainlayout)

    def remove_widget(self):
        #remove the orignal widget under the content_widget layout
        for i in reversed(range(self.content_widget_layout.count())): 
            self.content_widget_layout.itemAt(i).widget().deleteLater()

    def add_widget(self, widget_list):
        self.remove_widget()

        self.widget_list = []
        for widget in widget_list:
            checkbox = label_checkbox(widget[0], widget[1])
            self.widget_list.append(checkbox)
            self.content_widget_layout.addWidget(checkbox)

        self.all_checkbox = label_checkbox("All")
        self.all_checkbox.stateChanged.connect(self.all_checkbox_function)
        
        #update the height of content_widget
        self.content_widget_layout.addWidget(self.all_checkbox)
        self.content_widget.setFixedHeight(((len(self.widget_list)+1)*int(self.all_checkbox.height()) + 4))
  
        self.content_widget.update()
        self.update()
    
    def all_checkbox_function(self):
        if self.all_checkbox.isChecked():      
            for widget in self.widget_list:
                widget.setChecked(True)
        else:
            for widget in self.widget_list:
                widget.setChecked(False)

    def no_result(self):
        self.remove_widget()
        
        self.widget_list = []
        self.result_label = QLabel()
        self.result_label.setText("No related csv file was found")
        self.result_label.setFixedHeight(25)
        self.result_label.setStyleSheet(
            '''
                QLabel{
                font:bold 14px;
                color:#000000;
                }
            ''')
        
        #update the height of content_widget
        self.content_widget_layout.addWidget(self.result_label)
        self.content_widget.setFixedHeight((self.result_label.height() + 4))

        self.content_widget.update()
        self.update()

    def file_selection(self):
        self.widget_selection = []
        for widget in self.widget_list:
            if widget.isChecked():
                self.widget_selection.append(widget)

        return self.widget_selection

class groupbox_3_for_MainPage(QGroupBox):
    def __init__(self):
       super(self.__class__, self).__init__()
       self.setMinimumHeight(70)
       self.initUI()

    def initUI(self):
        self.setTitle("Step 3: Confirm the files selection? (Try not to select more than ten files once)")
        self.setStyleSheet(
            '''
               QGroupBox{
               font:bold 14px;
               color:#000000;
               background-color: #f1f1f1;
               }
            '''
            )

        #Create two pushbutton
        self.process_button = Process_button_2("Select")
        self.reset_button = Process_button_2("Reset")

        #Create a qhboxlayout for the two button
        self.mainlayout = QHBoxLayout()
        self.mainlayout.addSpacing(200)
        self.mainlayout.addWidget(self.process_button)
        self.mainlayout.addWidget(self.reset_button)
        self.mainlayout.addStretch()
        self.mainlayout.setSpacing(30)
        self.mainlayout.setContentsMargins(15, 4, 15, 4)

        self.setLayout(self.mainlayout)

class groupbox_4_for_FunctionPage(QGroupBox):
    def __init__(self, title = ""):
        super(self.__class__, self).__init__()
        self.title = title
        self.initUI()
        self.filepath = None
        self.widget_list = []

    def initUI(self):
        self.setTitle(self.title)
        self.setMinimumWidth(750)
        self.setStyleSheet(
            '''
                QGroupBox{
                font:bold 14px;
                color:#000000;
                background-color: #f1f1f1;
                }
            '''
            )
        
        #create the mainlayout 
        self.mainlayout = QVBoxLayout()
        self.mainlayout.setSpacing(5)
        self.mainlayout.setContentsMargins(90, 4, 30, 4)
        self.setLayout(self.mainlayout)

    def remove_widget(self):
        for i in reversed(range(self.mainlayout.count())): 
            self.mainlayout.itemAt(i).widget().deleteLater()
    
    def update_widget(self, filepath, widget_list, widget_with_date_list):
        self.remove_widget()
        self.filepath = filepath
        self.widget_list = widget_list

        for name in widget_with_date_list:
            widget = File_Label(name)
            self.mainlayout.addWidget(widget)
        self.mainlayout.update()

class groupbox_5_for_FunctionPage(QGroupBox):
    def __init__(self, description = "", _type = int(0), calendar_type = int(0)):
        super(self.__class__, self).__init__()
        self.description = description
        self._type = _type
        self.calendar_type = calendar_type
        self.initUI()

    def initUI(self):
        self.setTitle(self.description)
        self.setMinimumHeight(70)
        self.setStyleSheet(
            '''
                QGroupBox{
                font:bold 14px;
                color:#000000;
                background-color: #f1f1f1;
                }
            '''
            )
        
        #create a button
        self.pushbutton = Process_button_2("Process")

        #create the mainlayout
        self.mainlayout = QHBoxLayout()
        
        #check if it needs to add widget
        if self._type == 1:
            self.mainlayout.addSpacing(200)
            self.add_date_input_widget()
            self.mainlayout.setSpacing(10)
        elif self._type == 2:
            self.mainlayout.addSpacing(100)
            self.mainlayout.setSpacing(0)
            self.add_two_date_input_widget()
            self.mainlayout.addSpacing(10)
        else:
            self.mainlayout.addSpacing(200)
            self.mainlayout.setSpacing(10)

        self.mainlayout.addSpacing(20)
        self.mainlayout.addWidget(self.pushbutton)
        self.mainlayout.addStretch()
        self.mainlayout.setContentsMargins(0, 2, 0, 2)

        self.setLayout(self.mainlayout)

    def add_date_input_widget(self):
        #create a qlineedit for entering the date
        self.DateLineEdit_Calendar = DateLineEdit_Calendar(calendar_type = self.calendar_type)
        self.mainlayout.addWidget(self.DateLineEdit_Calendar)

    def add_two_date_input_widget(self):
        #create two qlineedits for entering the date
        self.DateLineEdit_Calendar_1 = DateLineEdit_Calendar()
        self.DateLineEdit_Calendar_2 = DateLineEdit_Calendar()
   
        self.label_1 = QLabel()
        self.label_1.setFixedSize(45, 25)
        self.label_1.setText("From")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setStyleSheet(
            '''
                QLabel{
                font:14px;
                font-weight:bold;
                }
            '''
            )
        
        
        self.label_2 = QLabel()
        self.label_2.setFixedSize(30, 25)
        self.label_2.setText("To")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setStyleSheet(
            '''
                QLabel{
                font:14px;
                font-weight:bold;
                }
            '''
            )
        
        self.mainlayout.addWidget(self.label_1)
        self.mainlayout.addWidget(self.DateLineEdit_Calendar_1)
        self.mainlayout.addWidget(self.label_2)
        self.mainlayout.addWidget(self.DateLineEdit_Calendar_2)
        
class groupbox_6_for_FunctionPage(QGroupBox):
    def __init__(self, title = "Result:"):
        super(self.__class__, self).__init__()
        self.title = title
        self.initUI()

    def initUI(self):
        self.setTitle(self.title)
        self.setMinimumHeight(500)
        self.setStyleSheet(
            '''
                QGroupBox{
                font:bold 14px;
                color:#000000;
                background-color: #f1f1f1;
                }
            '''
            )

        #create a qtextedit
        self.data = QTextEdit()
        self.data.setStyleSheet(
            '''
            QTextEdit{
            font: 13px;
            }
            '''
            )

        #create the mainlayout
        self.mainlayout = QVBoxLayout()
        self.mainlayout.addWidget(self.data)
        self.mainlayout.setContentsMargins(15, 6, 15, 10)

        self.setLayout(self.mainlayout)

class File_Label(QLabel):
    def __init__(self, text = ""):
        super(self.__class__, self).__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 20)
        self.setText(self.text)
        self.setStyleSheet(
            ''' 
                QLabel
                    {
                    background-color:#f5b380;
                    color: #000000;
                    font:bold 12px;
                    }
            ''')
        self.setAlignment(Qt.AlignCenter)

class label_checkbox(QCheckBox):
    def __init__(self, text_1 = "", text_2 = ""):
        super(self.__class__, self).__init__()
        self.text_1 = text_1
        self.text_2 = text_2

        self.initUI()

    def initUI(self):
        self.setFixedHeight(25)
        if self.text_2 != "":
            self.setText(self.text_1 + "    -" + self.text_2)
        else:
            self.setText(self.text_1)

        self.setStyleSheet(
            '''
                QCheckBox
                    {
                    font-size:15px;
                    color: #000000;
                    }
                QCheckBox:checked
                    {
                    color: #e3681b;
                    }
                QCheckBox::indicator 
                    {
                    subcontrol-position: left center;
                    subcontrol-origin: padding;
                    bottom: -1px;
                    }
            ''')

class Process_button(QPushButton):
    def __init__(self, text = "Sample"):
        super(self.__class__, self).__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        self.setFixedSize(65, 25)
        self.setText(self.text)
        self.setStyleSheet(
            ''' 
                QPushButton
                    {
                    background-color:#f5b380;
                    color: #000000;
                    font-size: 14px;
                    }
                QPushButton:hover
                    { 
                    background-color: #FFB782;
                    font-size: 15px;
                    font-weight:bold;
                    }
                QPushButton:pressed
                    {
                    color: #eeeeee;
                    }
            ''')

class Process_button_2(QPushButton):
    def __init__(self, text):
        super(self.__class__, self).__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        self.setText(self.text)
        self.setFixedSize(130, 30)
        self.setStyleSheet(
            ''' 
                QPushButton
                    {
                    background-color:#f5b380;
                    color: #000000;
                    font-size: 14px;
                    }
                QPushButton:hover
                    { 
                    background-color: #FFB782;
                    font-size: 15px;
                    font-weight:bold;
                    }
                QPushButton:pressed
                    {
                    color: #eeeeee;
                    }
            ''')

class main_progress_bar(QProgressBar):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 20)
        self.setStyleSheet(
            '''
            QProgressBar{
            border: 1px solid grey;
            border-radius: 5px;
            text-align: center;
            color: #000000;
            }
            QProgressBar::chunk{
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                      stop: 0 #bbedc0, stop: 1 #319941);
            }
            ''')

class file_path_widget(QWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(550, 25)
        
        self.FilePath = QLineEdit()
        self.FilePath.setFixedSize(530, 25)
        self.FilePath.setStyleSheet(
            '''
                QLineEdit{
                font:14px;
                }
            ''')

        self.open_file_button = Process_button("...")
        self.open_file_button.pressed.connect(self.open_file_button_function)
        self.open_file_button.setFixedSize(20, 25)

        self.mainlayout = QHBoxLayout()
        self.mainlayout.addWidget(self.FilePath)
        self.mainlayout.addWidget(self.open_file_button)
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mainlayout)
        
    def open_file_button_function(self):
        fn = QFileDialog()
        path = fn.getExistingDirectory(self, 'Select Folder', options=QFileDialog.DontUseNativeDialog)
        self.FilePath.setText(path)
        self.run_scan_button_function()

    def run_scan_button_function(self):
        pass

class PasswdDialog(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 200)

        self.name_label = QLabel("User:")
        self.name_label.setFixedSize(90, 25)
        self.name_label.setStyleSheet(
            '''
            QLabel{
            color:#523c00;
            font:bold 14px;
            }
            ''')

        self.textName = QLineEdit()
        self.textName.setFixedSize(200, 25)
        self.textName.setStyleSheet(
            '''
            QLineEdit{
            font:14px;
            }
            ''')

        self.first_layout = QHBoxLayout()
        self.first_layout.addWidget(self.name_label)
        self.first_layout.addWidget(self.textName)
        self.first_layout.setSpacing(5)
        self.first_layout.addStretch()
        self.first_layout.setContentsMargins(0, 0, 0, 0)
        
        self.password_label = QLabel("Password:")
        self.password_label.setFixedSize(90, 25)
        self.password_label.setStyleSheet(
            '''
            QLabel{
            color:#523c00;
            font:bold 14px;
            }
            ''')
     
        self.textPass = QLineEdit()
        self.textPass.setEchoMode(QLineEdit.Password)
        self.textPass.setFixedSize(200, 25)
        self.textPass.setStyleSheet(
            '''
            QLineEdit{
            font:14px;
            }
            ''')

        self.second_layout = QHBoxLayout()
        self.second_layout.addWidget(self.password_label)
        self.second_layout.addWidget(self.textPass)
        self.second_layout.setSpacing(5)
        self.second_layout.addStretch()
        self.second_layout.setContentsMargins(0, 0, 0, 0)
        
        self.echopassword_checkbox = QCheckBox()
        self.echopassword_checkbox.setText("show")
        self.echopassword_checkbox.stateChanged.connect(self.set_echo)
        self.echopassword_checkbox.setFixedSize(60, 14)
        self.echopassword_checkbox.setStyleSheet(
            '''
            QCheckBox{
            font:11px;
            }
            ''')       
        self.third_layout = QHBoxLayout()
        self.third_layout.addWidget(self.echopassword_checkbox)
        self.third_layout.setSpacing(5)
        self.third_layout.addStretch()
        self.third_layout.setContentsMargins(95, 0, 0, 0)
        
        self.buttonLogin = Process_button_2("Login")
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonLogin.setFixedSize(100, 30)
        
        self.buttonClear = Process_button_2("Clear")
        self.buttonClear.pressed.connect(self.clear_text)
        self.buttonClear.setFixedSize(100, 30)

        self.buttonSkip = Process_button_2("Skip")
        self.buttonSkip.pressed.connect(self.skip)
        self.buttonSkip.setFixedSize(100, 30)

        self.fourth_layout = QHBoxLayout()
        self.fourth_layout.addWidget(self.buttonLogin)
        self.fourth_layout.addWidget(self.buttonClear)
        self.fourth_layout.addWidget(self.buttonSkip)
        self.fourth_layout.setSpacing(5)
        self.fourth_layout.addStretch()
        self.fourth_layout.setContentsMargins(0, 0, 0, 0)

        self.buttonLogin = Process_button_2("Login")
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.first_layout)
        self.layout.addLayout(self.second_layout)
        self.layout.addLayout(self.third_layout)
        self.layout.addLayout(self.fourth_layout)
        self.layout.setSpacing(25)
        self.layout.addStretch()
        self.layout.setContentsMargins(35, 35, 35, 25)
        self.setLayout(self.layout)

    def handleLogin(self):
        if (self.textName.text() == "Bart" and self.textPass.text() == "123456"):
            self.accept()

        else:
            message = QMessageBox()
            try:
                message.setWindowIcon(QIcon('image\main_icon.png'))
            except:
                pass
            message.warning(self, "Error", "Wrong username or password, Please Try again!")

    def clear_text(self):
        self.textName.setText("")
        self.textPass.setText("")

    def set_echo(self):
        if self.echopassword_checkbox.isChecked() == True:
            self.textPass.setEchoMode(QLineEdit.Normal)
        elif self.echopassword_checkbox.isChecked() == False:
            self.textPass.setEchoMode(QLineEdit.Password)

    def skip(self):
        self.accept()

class Error(Exception):
    pass

class EmptyValueError(Error):
    pass

class YearTransferError(Error):
    pass

class Calendar(QCalendarWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calendar")
        try:
            self.setWindowIcon(QIcon('image\calendar.png'))
        except:
            pass

    def get_date(self):
        print (self.selectedDate())

class DateLineEdit_Calendar(QWidget):
    def __init__(self, calendar_type = int(0)):
        super(self.__class__, self).__init__()
        #calendar_type to int(0): set date format to "yyyy-MM-dd"
        #calendar_type to 1nt(1): set date format to "yyyy"

        self.calendar_type = calendar_type
        self.initUI()

    def initUI(self):
        self.setFixedSize(140, 25)
        self.date_input = QLineEdit()
        self.date_input.setFixedSize(120, 25)
        self.date_input.setStyleSheet(
            '''
                QLineEdit{
                font:14px;
                }
            ''')

        self.open_calendar_button = Process_button("...")
        self.open_calendar_button.setFixedSize(20, 25)
        
        self.CalendarWidget = Calendar()
        self.CalendarWidget.clicked.connect(self.get_date)
        self.open_calendar_button.pressed.connect(self.open_calendar_button_function)

        #set mainlayout
        self.mainlayout = QHBoxLayout()
        self.mainlayout.addWidget(self.date_input)
        self.mainlayout.addWidget(self.open_calendar_button)
        self.mainlayout.setSpacing(0)
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)
    
    def open_calendar_button_function(self):
        #button_location = self.open_calendar_button.pos()

        if self.CalendarWidget.isHidden():
            self.CalendarWidget.show()
            #self.CalendarWidget.move(button_location)
        else:
            self.CalendarWidget.hide()
            #self.CalendarWidget.move(button_location)

    def get_date(self):
        if self.calendar_type == int(0):
            self.date_input.setText(self.CalendarWidget.selectedDate().toString("yyyy-MM-dd"))
        elif self.calendar_type == int(1):
            self.date_input.setText(self.CalendarWidget.selectedDate().toString("yyyy"))

#--------------------------------------------------------------
#--------------------------------------------------------------
#--      __            __ ___    __           __   __  ___   -- 
#--     |__ |  | |\ | |    |  | |  | |\ |    |__  |__   |    --
#--     |   |__| | \| |__  |  | |__| | \|     __| |__   |    -- 
#--------------------------------------------------------------
#--------------------------------------------------------------

#This is all the function set

#scan how many csv files in the file path
def detect_csv(filepath):
    file_name_list = []
    for dirpath, dirname, files in os.walk(filepath):
        for file in files:
            if file.endswith(".csv"):
                #get the basic information of the csv file
                statusbuf = os.stat(os.path.join(dirpath, file))
                
                #get the modified time of the csv file
                file_modified_time = datetime.fromtimestamp(statusbuf.st_mtime).strftime("%b-%d-%Y %I:%M:%S %p")
                file_name_list.append([file, file_modified_time])

        
    return filepath, file_name_list

def read_csv(filepath, file_name):
    datadic = {}
    for file in file_name:
        file_dir = os.path.join(filepath, file) 
        
        with open(file_dir, "r") as csv_file:
            data_reader = csv.reader(csv_file, delimiter = ',')
            
            #skip the Header
            first_row = next(data_reader, None)
            
            datadic.update({file:list(data_reader)})

    return datadic

def get_maximum(datadic, progress_bar_value, progress_bar):
    
    temp_text = ""
    
    temp_text += "\nThis is to get the maximum value of the stock\n"

    try:
        for key, value in datadic.items():
            temp_text += "\n\nReading File: " + "------"+ key + "------\n"

            maximum_value = float(0)

            for row in value:
                if maximum_value < float(row[2]):
                    maximum_value = float(row[2])

            for row in value:
                if float(row[2]) == maximum_value:
                    temp_text += "\n\tdate:     {}".format(row[0])
                    temp_text += "\n\topen:     {}".format(row[1])
                    temp_text += "\n\tday_high: {}".format(row[2])
                    temp_text += "\n\tday_low:  {}".format(row[3])
                    temp_text += "\n\tclose:    {}".format(row[4])
                    try:
                        temp_text += "\n\tvolume:   {}".format(row[5])
                    except Exception:
                        temp_text += "\n\tvolume:      -"

            progress_bar_value += 1
            progress_bar.setValue(progress_bar_value)  
    
    except Exception as e:
        temp_text += str(e)

    return temp_text

def get_data_from_date(datadic, new_date, progress_bar_value, progress_bar):
    
    Error_type_1 = EmptyValueError()
    temp_text = ""

    #format new_date to datetime
    try:
        if new_date == "":
            raise Error_type_1

        try:
            formated_new_date = datetime.strptime(new_date, "%Y-%m-%d")
        except:
            raise YearTransferError

        for key, value in datadic.items():
            
            temp_text += "\n\nReading File: " + "------"+ key + "------\n"
            
            date_set = OrderedDict()

            #create a new date_set, key is format to datetime of its date, value is the row value
            for row in value:
                formated_date = datetime.strptime(row[0], "%Y-%m-%d")
                
                #check how many row objects
                if len(row) == 6:
                    date_set.update({formated_date:[row[0], row[1], row[2], row[3], row[4], row[5]]})
                else:
                    date_set.update({formated_date:[row[0], row[1], row[2], row[3], row[4]]})
            
            #check if the users date has any data or not
            if formated_new_date in date_set:
                temp_text += "\n\tdate:     {}".format(date_set[formated_new_date][0])
                temp_text += "\n\topen:     {}".format(date_set[formated_new_date][1])
                temp_text += "\n\tday_high: {}".format(date_set[formated_new_date][2])
                temp_text += "\n\tday_low:  {}".format(date_set[formated_new_date][3])
                temp_text += "\n\tclose:    {}".format(date_set[formated_new_date][4])
                
                #check how many row objects
                if len(date_set[formated_new_date]) == 6:
                    temp_text += "\n\tvolume:   {}".format(row[5])
                else:
                    temp_text += "\n\tvolume:      -" 
                
            else:
                previous_date = formated_new_date
                next_date = formated_new_date
                
                while next_date not in date_set:
                    if next_date - list(date_set.keys())[-1] > timedelta(days = 0):
                        break
                    else:
                        next_date += timedelta(days = 1)


                while previous_date not in date_set:
                    if previous_date - list(date_set.keys())[0] < timedelta(days = 0):
                        break
                    else:
                        previous_date -= timedelta(days = 1)
                
                temp_text += "\n\tNo related data is found, please input another date."
                
                if previous_date == formated_new_date :
                    previous_date = next_date
                    temp_text += "\n\tThe closest date is {0}".format(str(next_date.strftime("%Y-%m-%d")))
                elif next_date == formated_new_date:
                    temp_text += "\n\tThe closest date is {0}".format(str(previous_date.strftime("%Y-%m-%d")))
                else:
                    temp_text += "\n\tThe closest date are {0} and {1}".format(str(previous_date.strftime("%Y-%m-%d")), str(next_date.strftime("%Y-%m-%d")))
            
            progress_bar_value += 1
            progress_bar.setValue(progress_bar_value)
     
    except EmptyValueError:
        temp_text += "\n\tYou didn't input any date, please check it again!"
    
    except YearTransferError:
        temp_text += "\n\tCan not transfer to the correct date, please check it again!"
    
    except Exception as e:
        temp_text += str(e)

    return temp_text

def get_week_value(datadic, progress_bar_value, progress_bar):
    temp_text = ""
    temp_text += "\nThis is to get value at the end of each value"
    
    #Step 1:Get the file to process
    for key, value in datadic.items():
        
        temp_text += "\n\nReading File: " + "------" + key + "------\n"

        #Step 2: adjust list by the week, and adjust the data type in module: datetime
        date_list = [datetime.strptime(row[0], "%Y-%m-%d") for row in value]

        oldest_date_of_each_week = data_adjust_by_week(date_list)
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 3: find out the max date of each week
        date_and_value = []
        for row in value:
            date_format = datetime.strptime(row[0], "%Y-%m-%d")
            for day in oldest_date_of_each_week:
                if date_format == day[1]:
                    date_and_value.append([row[0], row[4]])

        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)
        
        #Step 4: calculate the increase_rate
        count_positive = 0
        count_negative = 0
        for num in range(len(date_and_value) - 1):
            increase_rate = Decimal(date_and_value[num + 1][1])/Decimal(date_and_value[num][1])*100 - 100
            increase_rate = increase_rate.quantize(Decimal("0.00000"))
            if increase_rate > 0:
                count_positive += 1
            elif increase_rate < 0:
                count_negative += 1

            date_and_value[num + 1].append("{0}%".format(increase_rate))
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 5:print out the data   
        for data in date_and_value:
            if len(data) == 2:
                temp_text += "\n\tdate: {0}\tclose: {1}".format(data[0], data[1])              
            elif len(data) == 3:
                temp_text += "\n\tdate: {0}\tclose: {1}\t\trate: {2}".format(data[0], data[1], data[2])
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 6:print out the num of the positive increase_rate:
        positive_rate = Decimal(count_positive)/(count_positive + count_negative)*100
        negative_rate = Decimal(count_negative)/(count_positive + count_negative)*100
        temp_text += "\n\n\tThe num of positive rate: {0}  {1}%".format(count_positive, positive_rate.quantize(Decimal("0.00000")))
        temp_text += "\n\tThe num of negative rate: {0}  {1}%".format(count_negative, negative_rate.quantize(Decimal("0.00000")))

    return temp_text

def get_month_value(datadic, progress_bar_value, progress_bar):
    temp_text = ""
    temp_text += "\nThis is to get value at the end of each month"

    #Step 1: Get file to process
    for key, value in datadic.items():                        
        temp_text += "\n\nReading File: " + "------" + key + "------\n"
        
        #Step 2: adjust list by the month, and adjust the data type into module: datetime
        date_list = [datetime.strptime(row[0], "%Y-%m-%d") for row in value]
        
        oldest_date_of_each_month = data_adjust_by_month(date_list)
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 3: find out the max date of each month
        date_and_value = []
        for row in value:
            date_format = datetime.strptime(row[0], "%Y-%m-%d")
            for day in oldest_date_of_each_month:
                if date_format == day[1]:
                    date_and_value.append([row[0], row[4]])
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 4: calculate the increase_rate
        count_positive = 0
        count_negative = 0
        for num in range(len(date_and_value) - 1):
            increase_rate = Decimal(date_and_value[num + 1][1])/Decimal(date_and_value[num][1])*100 - 100
            increase_rate = increase_rate.quantize(Decimal("0.00000"))
            if increase_rate > 0:
                count_positive += 1
            elif increase_rate < 0:
                count_negative += 1

            date_and_value[num + 1].append("{0}%".format(increase_rate))

        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)
        
        #Step 5:print out the data   
        for data in date_and_value:
            if len(data) == 2:
                temp_text += "\n\tdate: {0}\tclose: {1}".format(data[0], data[1])              
            elif len(data) == 3:
                temp_text += "\n\tdate: {0}\tclose: {1}\t\trate: {2}".format(data[0], data[1], data[2])
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 6:print out the num of the positive increase_rate:
        positive_rate = Decimal(count_positive)/(count_positive + count_negative)*100
        negative_rate = Decimal(count_negative)/(count_positive + count_negative)*100
        temp_text += "\n\n\tThe num of positive rate: {0}  {1}%".format(count_positive, positive_rate.quantize(Decimal("0.00000")))
        temp_text += "\n\tThe num of negative rate: {0}  {1}%".format(count_negative, negative_rate.quantize(Decimal("0.00000")))

    return temp_text

def get_year_value(datadic, progress_bar_value, progress_bar):
    temp_text = ""
    temp_text += "\nThis is to get value at the end of each year"

    #Step 1: Get which file to process
    for key, value in datadic.items():                
        temp_text += "\n\nReading File: " + "------" + key + "------\n"
        
        #Step 2: adjust the list by years, and adjust the data type into module: datetime
        date_list = [datetime.strptime(row[0], "%Y-%m-%d") for row in value]

        oldest_date_of_each_year = data_adjust_by_year(date_list)
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 3: find out the max date of each year
        date_and_value = []
        for row in value:
            orignal_day = row[0]
            date_format = datetime.strptime(orignal_day, "%Y-%m-%d")
            for date in oldest_date_of_each_year:
                if date_format == date[1]:
                    date_and_value.append([row[0], row[4]])
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 4: calculate the increase_rate
        count_positive = 0
        count_negative = 0
        for num in range(len(date_and_value) - 1):
            increase_rate = Decimal(date_and_value[num + 1][1])/Decimal(date_and_value[num][1])*100 - 100
            increase_rate = increase_rate.quantize(Decimal("0.00000"))
            if increase_rate > 0:
                count_positive += 1
            elif increase_rate < 0:
                count_negative += 1
            date_and_value[num + 1].append("{0}%".format(increase_rate))
        
        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

        #Step 5:print out the data   
        for data in date_and_value:
            if len(data) == 2:
                temp_text += "\n\tdate: {0}\tclose: {1}".format(data[0], data[1])              
            elif len(data) == 3:
                temp_text += "\n\tdate: {0}\tclose: {1}\t\trate: {2}".format(data[0], data[1], data[2])

        positive_rate = Decimal(count_positive)/(count_positive + count_negative)*100
        negative_rate = Decimal(count_negative)/(count_positive + count_negative)*100
        temp_text += "\n\n\tThe num of positive rate: {0}  {1}%".format(count_positive, positive_rate.quantize(Decimal("0.00000")))
        temp_text += "\n\tThe num of negative rate: {0}  {1}%".format(count_negative, negative_rate.quantize(Decimal("0.00000")))

        progress_bar_value += 1
        progress_bar.setValue(progress_bar_value)

    return temp_text

def get_increase_rate_from_date_to_now(datadic, users_date, progress_bar_value, progress_bar):
    temp_text = ""

    if users_date == "":
        temp_text += "\n\tYou didn't input the year, please check it again!"
    else:
        #Step 1:Get file to process
        for key, value in datadic.items():                
            temp_text += "\n\nFile Name: ---{0}---\n".format(key)
            
            #Step 2: adjust the list by years, and adjust the data type into module: datetime
            date_list = [datetime.strptime(row[0], "%Y-%m-%d") for row in value]
            
            oldest_date_of_each_year = data_adjust_by_year(date_list)
            
            progress_bar_value +=1
            progress_bar.setValue(progress_bar_value)

            #Step 3: find out the data of the year which the users input, calculate the increase_rate
            signal = int(0)
            for data in oldest_date_of_each_year:
                if users_date == str(data[0].year):
                    
                    signal = int(1)
                    for row in value:
                        if data[0].strftime("%Y-%m-%d") == row[0]:
                            start_date = row[0]
                            start_value = Decimal(row[4])
                            signal = int(1)
                            
                        if oldest_date_of_each_year[-1][1].strftime("%Y-%m-%d") == row[0]:
                            end_date = row[0]
                            end_value = Decimal(row[4])
            
            progress_bar_value +=1
            progress_bar.setValue(progress_bar_value)

            #Step 4: print out the result        
            if signal == int(1):
                increase_rate = end_value/start_value*100 - 100

                temp_text += "\n\tEnd date: {0}\tValue: {1}\t\tRate: {2}%".format(end_date, end_value, increase_rate.quantize(Decimal("0.00000")))
            else:
                temp_text += "\n\tThe year is out of range of the csv files (the range is {0}-{1})".format(oldest_date_of_each_year[0][0].strftime("%Y"), oldest_date_of_each_year[-1][-1].strftime("%Y"))                

    return temp_text

def get_increase_rate_from_the_two_date(datadic, users_first_date, users_second_date, progress_bar_value, progress_bar):
    temp_text = ""

    if users_first_date == "" or users_second_date == "":
        temp_text += "\n\tYou didn't input the two dates, Please check it again"
    else:
        try:
            try:
                formated_users_first_date = datetime.strptime(users_first_date, "%Y-%m-%d")
                formated_users_second_date = datetime.strptime(users_second_date, "%Y-%m-%d")
            except:
                raise YearTransferError

            for key, value in datadic.items():
                
                temp_text += "\n\nFile Name: ---{0}---\n".format(key)

                date_set = OrderedDict()

                progress_bar_value +=1
                progress_bar.setValue(progress_bar_value)

                #Step 1:create a new date_set, key is format to datetime of its date, value is the row value
                for row in value:
                    formated_date = datetime.strptime(row[0], "%Y-%m-%d")

                    #check how many row objects
                    if len(row) == 6:
                        date_set.update({formated_date:[row[0], row[1], row[2], row[3], row[4], row[5]]})
                    else:
                        date_set.update({formated_date:[row[0], row[1], row[2], row[3], row[4]]})

                #Step 2:check if the first users date has any data or not
                if formated_users_first_date in date_set:
                    start_date = date_set[formated_users_first_date][0]
                    start_value = Decimal(date_set[formated_users_first_date][4])
                                       
                    temp_text += "\n\tStart date: {0}\tValue: {1}".format(start_date, start_value)
                else:
                    start_value = None
                    previous_date = formated_users_first_date
                    next_date = formated_users_first_date
                
                    while next_date not in date_set:
                        if next_date - list(date_set.keys())[-1] > timedelta(days = 0):
                            break
                        else:
                            next_date += timedelta(days = 1)


                    while previous_date not in date_set:
                        if previous_date - list(date_set.keys())[0] < timedelta(days = 0):
                            break
                        else:
                            previous_date -= timedelta(days = 1)
                    
                    temp_text += "\n\tStart date: {0}\tValue: {0}".format("Not Found")
                    
                    if previous_date == formated_users_first_date:
                        previous_date = next_date
                        temp_text += "\tThe closest date is {0}".format(str(next_date.strftime("%Y-%m-%d")))
                    elif next_date == formated_users_first_date:
                        temp_text += "\tThe closest date is {0}".format(str(previous_date.strftime("%Y-%m-%d")))
                    else:
                        temp_text += "\tThe closest date are {0} and {1}".format(str(previous_date.strftime("%Y-%m-%d")), str(next_date.strftime("%Y-%m-%d")))
                
                #Step 3:check if the second users date has any data or not
                if formated_users_second_date in date_set:
                    end_date = date_set[formated_users_second_date][0]
                    end_value = Decimal(date_set[formated_users_second_date][4])
                    temp_text += "\n\tEnd date: {0}\tValue: {1}".format(end_date, end_value)
                else:
                    end_value = None
                    previous_date = formated_users_second_date
                    next_date = formated_users_second_date
                
                    while next_date not in date_set:
                        if next_date - list(date_set.keys())[-1] > timedelta(days = 0):
                            break
                        else:
                            next_date += timedelta(days = 1)


                    while previous_date not in date_set:
                        if previous_date - list(date_set.keys())[0] < timedelta(days = 0):
                            break
                        else:
                            previous_date -= timedelta(days = 1)
                    
                    temp_text += "\n\tEnd date: {0}\tValue: {0}".format("Not Found")
                    
                    if previous_date == formated_users_second_date:
                        previous_date = next_date
                        temp_text += "\tThe closest date is {0}".format(str(next_date.strftime("%Y-%m-%d")))
                    elif next_date == formated_users_second_date:
                        temp_text += "\tThe closest date is {0}".format(str(previous_date.strftime("%Y-%m-%d")))
                    else:
                        temp_text += "\tThe closest date are {0} and {1}".format(str(previous_date.strftime("%Y-%m-%d")), str(next_date.strftime("%Y-%m-%d")))
                
                #Step 4:Print out the increase rate
                if end_value == None or start_value == None:
                    increase_rate = "----"
                else:
                    increase_rate = (end_value/start_value*100 - 100).quantize(Decimal("0.00000"))
                temp_text += "\n\tRate: {0}%".format(increase_rate)

        except YearTransferError:
            temp_text += "\n\tCan not transfer your input to the correct date, please check it again!"
        '''
        except Exception as e:
            temp_text += str(e)
        '''
    return temp_text

def data_adjust_by_week(date_list):
    #make a new list according to weeks, each row has a list with one or two or empty value: [min(week), max(week)]
    latest_year = max(date_list)
    oldest_year = min(date_list)
    
    #Step 1:make a full day list between the years
    total_days = latest_year - oldest_year
    full_day_list = []
    
    num = total_days
    sample_day = date_list[0]
    n = 0
    while n <= int(num.days):
        full_day_list.append(sample_day)
        n += 1
        sample_day = sample_day + timedelta(days =1)
    
    #Step 2: the first week is special, need to execute first
    first_week = []
    rest_of_list = []
    for n in range(8):
        if full_day_list[n].isoweekday() == 7:
            first_week = full_day_list[0:n+1]
            rest_of_list = full_day_list[n+1:]

    #Step 3:make a week list, each elements has seven days inside
    seven_day_list = [rest_of_list[x:x+7] for x in range(0, len(rest_of_list), 7)]
    seven_day_list.insert(0, first_week)
    
    #Step 4:make a new week list if it has valid value on that day according to the list which just created above
    week_adjust_list = []
    for row in seven_day_list:
        temp_list = []
        for row_s in row: 
            if row_s in date_list:
                temp_list.append(row_s)
        week_adjust_list.append(temp_list)

    #Step 5:make another new week list only has two elements of each row: the min and the max date of each week
    oldest_date_of_each_week= []
    for each_list in week_adjust_list:
        if each_list != []:
            oldest_date_of_each_week.append([min(each_list), max(each_list)])

    return oldest_date_of_each_week

def data_adjust_by_month(date_list):
    #make a new list according to months, each row has a list with two value: [min(month), max(month)]
    latest_year = max(date_list)
    oldest_year = min(date_list)
    date_list_adjust = []
    
    for year in range(int(oldest_year.year), int(latest_year.year)+1):
        for month in range(1, 13):
            date_same_year_month = [date for date in date_list if date.year == year and date.month == month]

            if date_same_year_month != []:
                date_list_adjust.append(date_same_year_month)
    
    oldest_date_of_each_month= []
    for each_list in date_list_adjust:
        oldest_date_of_each_month.append([min(each_list), max(each_list)])

    return oldest_date_of_each_month

def data_adjust_by_year(date_list):
    #make a new list according to years, each row has a list with two value: [min(year), max(year)]
    latest_year = max(date_list)
    oldest_year = min(date_list)
    date_list_adjust = []
    
    for year in range(int(oldest_year.year), int(latest_year.year)+1):
        date_same_year = [date for date in date_list if date.year == year]
        
        if date_same_year != []:
            date_list_adjust.append(date_same_year)
    
    oldest_date_of_each_year= []
    for each_list in date_list_adjust:
        oldest_date_of_each_year.append([min(each_list), max(each_list)])

    return oldest_date_of_each_year

def last_day_of_month(date_input):
    if date_input.month == 12:
        return date_input.replace(day = 31)
    return date_input.replace(month = date_input.month + 1, day = 1) - timedelta(days =1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = PasswdDialog()
    try:
        Login.setWindowIcon(QIcon('image\main_icon.png'))
    except:
        pass
    
    Login.show()
    if Login.exec_() == QDialog.Accepted:
        win = MainWindow()
        try:
            win.setWindowIcon(QIcon('image\main_icon.png'))
        except:
            pass
        win.show()
    app.exec_()
