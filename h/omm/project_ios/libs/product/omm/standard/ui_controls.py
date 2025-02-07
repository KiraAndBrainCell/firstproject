import traceback
from libs.product.omm.standard import global_vars
from libs.product.omm.standard import omm_lib
from libs.product.omm.standard import util

g = global_vars
get_obj_identifier = omm_lib.get_obj_identifier
CurrentElementnameforselection=None
CurrentElementidentifierforselection=None
Uipagescrollcount=0



class ui_controls():

	def ui_element(self, identifier_property, tag_name=None):
		"""
		This function is used for getting any UI element

		Function Owner : Nithya_V

		Date created : 20/04/2016

		@param  identifier_property : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
				(Eg: class, id, name etc)
	
		@return element : (object) returns element if object found, else returns None
		"""
		element= None
		try :
			# getting tag and unique of the object to be identified
			tag, identifier_val = omm_lib.get_tag_identifier(identifier_property, tag_name)
			# finding element based on the tag name provided by user
			if tag == 'id':
				element = g.driver.find_element_by_id(identifier_val)
			elif tag == 'name':
				element = g.driver.find_element_by_name(identifier_val)
			elif tag == 'class':
				element = g.driver.find_element_by_class_name(identifier_val)
			elif tag == 'xpath':
				element = g.driver.find_element_by_xpath(identifier_val)

			print "Element with tag %s and identifier %s is found\n" % (tag, identifier_val)
		except:
			traceback.print_exc()
			print "Element with tag %s and identifier %s is not found\n" % (tag, identifier_val)
			element = None
		return element
	
	def ui_elements(self, identifier_property, tag_name=None):
		"""
		This function is used for getting multiple UI elements
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016
		
		@param  identifier_property : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return elements : (object list) returns multiple elements matching property, else returns None
		"""
		elements= []
		try :
			# getting tag and unique of the object to be identified
			tag, identifier_val = omm_lib.get_tag_identifier(identifier_property, tag_name)

			# finding element based on the tag name provided by user
			if tag == 'id':
				elements = g.driver.find_elements_by_id(identifier_val)
			elif tag == 'name':
				elements = g.driver.find_elements_by_name(identifier_val)
			elif tag == 'class':
				elements = g.driver.find_elements_by_class_name(identifier_val)

			print "Element with tag %s and identifier %s is found\n" % (tag, identifier_val)
		except:
			traceback.print_exc()
			print "Element with tag %s and identifier %s is not found\n" % (tag, identifier_val)
			elements = []
		return elements
	
	def text_box(self, identifier, value=None, tag_name=None):
		"""
		This function is used for entering text into a text field, reads the text in a text field
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016
	
		@param  identifier : (String) Object property fetched from object repository
		@param  value : (String) Value to be edited
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
							Returns text field value, if value is None
		"""
		try:
			# getting text box element
			text_box_element = self.ui_element(identifier, tag_name)
			
			# if value is provided and element is enabled, new values will be set
			if value is not None:
				if text_box_element.is_enabled():
					text_box_element.clear()
					text_box_element.send_keys(value)
					print "Text box with identifier %s is edited with value %s \n" % (identifier, value)
				else :
					#fails if value is provided and element is disabled
					assert(),"Text box element '%s' is in disabled state, hence no enter value is possible" % identifier

			# if value is None, element current value is returned
			elif value is None :
				return text_box_element.get_attribute("value").encode("ascii", "ignore")
		except:
			traceback.print_exc()
			return False
		return True
	#def update_setings(self, settings, vlue):
		
		"""
		This function is used to scroll down
	
		Function Owner : Nagarjuna
	
		Date created : 20/04/2016

		"""
	    #try:
			# if keyboard presence check is not required, hides keyboards only when it is present
		    #g.driver.update_settings({"some settings":"the value"})
		#except:
			#traceback.print_exc()
			#return False
		#return True
	def updte_setngs(self):
		"""
		This function is used for hide keyboard based on presence of keyboard
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		@param  check_keyboard_presence : (bool) True if hide keyboard has to be performed
										only when keyboard presence is detected
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			  
				# checks keyboard presence whether it is present or absent
				#g.driver.switch_to_alert().accept()
				g.driver.update_settings({"autoAcceptAlerts":"False"})
		except:
			traceback.print_exc()
			return False
		return True    

	def check_box(self, identifier, value='check', tag_name=None, plainChkUnchk=False):
		"""
		This function will check/ uncheck check box element present in UI
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016
		
		@param  identifier : (String) Object property fetched from object repository
		@param  value : (String) check / uncheck - action to be performed on check box
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
							Returns text field value, if value is None
		"""
		try:
			# getting check box element
			checkBoxElement = self.ui_element(identifier, tag_name)
			
			if plainChkUnchk:
				checkBoxElement.click()
				print "Check box element is clicked"
				return True

			# checks/ unchecks if element is enabled
			if checkBoxElement.is_enabled():
				if (value == "check"):
					
					# do nothing if it is already selected, else selects check box
					if (checkBoxElement.is_selected()):
						print "Check box element with identifier %s is already selected\n" % identifier
					else:
						try :
							checkBoxElement.click()
							print "Check box element with identifier %s is selected\n" % identifier
						except Exception,e:
							assert(),"Failed with error message %s" %e
							return False
				elif (value == "uncheck"):
					
					# do nothing if it is already unselected, else deselects check box
					if (checkBoxElement.is_selected()):
						try :
							checkBoxElement.click()
							print "Check box element with identifier %s is unchecked\n" % identifier
						except Exception,e:
							assert(),"Failed with error message %s" % e
							return False
					else:
						print "Check box element with identifier %s is already unchecked\n" % identifier
			else :
				assert(),"Check box element '%s' is in disabled state, hence no check or un-check is possible" % identifier
		except:
			traceback.print_exc()
			return False
		return True

	def hide_keyboard(self, check_keyboard_presence=False):
		"""
		This function is used for hide keyboard based on presence of keyboard
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		@param  check_keyboard_presence : (bool) True if hide keyboard has to be performed
										only when keyboard presence is detected
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# if keyboard presence check is not required, hides keyboards only when it is present
			if check_keyboard_presence == False:
				try:
					g.driver.hide_keyboard()
				except:
					pass
			else:
				# checks keyboard presence whether it is present or absent
				g.driver.hide_keyboard()
		except:
			traceback.print_exc()
			return False
		return True
	
	def scroll_element(self, x_elem, y_elem):
		"""
		This function is used for scrolling from x element to y element
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016
		
		@param  x_elem : (object) source element from which scroll has to start
		@param  y_elem : (object) destination element to which scroll has to end
		
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# scrolls element from one location to another
			g.driver.scroll(x_elem, y_elem)
		except:
			traceback.print_exc()
			return False
		return True

	def setValue(self, identifier, value, tag_name=None):
		"""
		This function is used for setting value on an element (eg: textbox) which
		may not work with send_keys method
	
		Function Owner : Nithya_V
	
		Date created : 17/05/2016
		
		@param  value : (string) value to be set on the element
		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
		
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			element = self.ui_element(identifier, tag_name)
				
			# set value of element
			g.driver.set_value(element, value)
		except:
			traceback.print_exc()
			return False
		return True

	def button(self, identifier, tag_name=None):
		"""
		This function is used for clicking on a button if it is enabled
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# getting the button element
			element_button = self.ui_element(identifier, tag_name)
			
			# clicks element only when it is enabled, else fails
			if element_button.is_enabled():
				element_button.click()
				print "Button element with identifier %s is clicked\n" % identifier
			elif (not element_button.is_enabled()):
				assert(),"Button '%s' is grayed out " % identifier
				return False
		except:
			traceback.print_exc()
			return False
		return True		

	def text_view(self, identifier, tag_name=None, value=None,label=None):
		"""
		This function is used for getting text from text view
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return text : (status) returns text from text view, None if no text
		"""
		text = None
		try:
			# getting the button element
			textView = self.ui_element(identifier, tag_name)
			if value:
				text = textView.get_attribute('value').encode("ascii", "ignore")
			elif label:
				text = textView.get_attribute('label').encode("ascii", "ignore")
			else:
				text = textView.get_attribute('text').encode("ascii", "ignore")
			print "text is %s\n" % text
		except:
			traceback.print_exc()
			return None
		return text


	def label(self, identifier, tag_name = None):
		"""
		This function is used to check if label exists
	
		Function Owner : Pooja_Rundwal
	
		Date created : 02/05/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			element_label = self.ui_element(identifier, tag_name)
			if element_label.is_enabled():
				print "label with identifier %s exists\n" % identifier
			elif (not element_label.is_enabled()):
				assert(),"Label'%s' does not exist " % identifier
				return False
		except:
			traceback.print_exc()
			return False
		return True


	def progressbar_value(self, identifier, tag_name = None):
		"""
		This function is used for getting progress bar value
	
		Function Owner : Pooja_Rundwal
	
		Date created : 20/04/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return value : (string) returns progress bar value
		"""
		value = None
		try:
			# getting the progress bar value
			progress_bar = self.ui_element(identifier, tag_name)
			value = progress_bar.get_attribute('value').encode("ascii", "ignore")
			print "progress bar value is %s" % value
		except:
			traceback.print_exc()
			return None
		return value


	def image(self, identifier, tag_name=None):
		"""
		This function is used for clicking on a image
	
		Function Owner : Pooja_Rundwal
	
		Date created : 09/06/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# getting the image element
			element_image= self.ui_element(identifier, tag_name)
			element_image.click()
			print "Image element with identifier %s is clicked\n" % identifier
		except:
			traceback.print_exc()
			return False
		return True

  
	 
	def capture_screenshot(self):
		try:
			screenshot_file_name = "screenshot_%s.png" % util.uniqueID()
			screenshot_path = g.screenshot_path + screenshot_file_name
			g.driver.save_screenshot(screenshot_path)
			print "\nFailure screenshot is captured to the logs file - File name %s\n" % screenshot_file_name
		except:
			traceback.print_exc()
			print "Could not capture the screenshot"
			
			
	def Click(self, identifier, tag_name=None):
		"""
		This function is used for clicking on any element 
	
		Function Owner : nagarjuna
	
		Date created : 20/04/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# getting the button element
			click_element = self.ui_element(identifier, tag_name)
			
			# clicks element only when it is enabled, else fails
			click_element.click()
		except:
			traceback.print_exc()
			return False
		return True		
	def isdisplayed(self, identifier, tag_name=None):
		"""
		This function is used check wteher element is displayed or not
	
		Function Owner : nagarjuna
	
		Date created : 20/04/2016

		@param  identifier : (String) Object property fetched from object repository
		@param  tag_name : (String) tag name of the identifier if any specific tag is required 
							(Eg: class, id, name etc)
	
		@return True/False : (status) returns True/False as per required action performed.
		"""
		try:
			# getting the button element
			click_element = self.ui_element(identifier, tag_name)
			
			# clicks element only when it is enabled, else fails
			click_element.is_displayed()
		except:
			traceback.print_exc()
			return False
		return True		
	
	def swipe_down(self):
		"""
		This function is used to scroll down
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		
		"""
		try:
			# if keyboard presence check is not required, hides keyboards only when it is present
			size = g.driver.get_window_size()
			starta=int(size["height"]*0.20)
			endz=int(size["height"]*0.60)
			startn=int(size["width"]/2)
			g.driver.swipe(startn,endz,startn,starta,900)
		except:
			
			traceback.print_exc()
			return False
		return True	
	
	def back_button(self):
		"""
		This function is used to go backbutton
	
		Function Owner : Nithya_V
	
		Date created : 20/04/2016

		
		"""
		try:
			# if keyboard presence check is not required, hides keyboards only when it is present
			
				
			g.driver.keyevent(4)
		except:
			
			traceback.print_exc()
			return False
		return True
	

	
	def swipe_up(self):
		
		"""
		This function is used to scroll down
	
		Function Owner : Nagarjuna
	
		Date created : 20/04/2016

		"""
		try:
			# if keyboard presence check is not required, hides keyboards only when it is present
			size = g.driver.get_window_size()

			starta=int(size["height"]*0.20)
			
			endz=int(size["height"]*0.60)
			
			startn=int(size["width"]/2)
			
			g.driver.swipe(startn,starta,startn,endz,900)
			
		except:
			
			traceback.print_exc()
			return False
		return True
	
	
	
	
	
	def ui_swipe_down_applicable(self):
		try:
			swipestatus=self.swipe_down()
			if swipestatus==True:
				print "Swipe status has been returned as true, we can still swipe the ui element,doing it now"
				self.ui_swipe_down_applicable()
			else:
				print "swipe status has been returned as false we can not swipe the ui element any more"					
		except:
			traceback.print_exc()
			return False
		return True	

	def Click_MultipleUIElements_Selectpassedelement(self, identifier, tag_name=None,Elementnameforselection=None,elementidentifier=None,elementname=None):

		"""
		This function is used to select an specific element once ui page is returning multiple elements with same resource id.
		Function Owner : Sudhish_Singh
		Date created :
		@param  identifier: (string) object identifier.
		@param  tag_name=None: (string) tag name.
		@param  Elementnameforselection: (string) element name which need to select from multiple elements.		
		@return status : (bool)status of execution.if successful True else False
		"""
		global Uipagescrollcount
		global CurrentElementidentifierforselection
		global CurrentElementnameforselection
		
		Uipagescrollcount = Uipagescrollcount+1
		print  "Function call count==>"+str(Uipagescrollcount)
		if Uipagescrollcount==1:
			CurrentElementidentifierforselection = elementidentifier
			CurrentElementnameforselection=elementname
					
		print "Click_MultipleUIElements_Selectpassedelement identifier===>"+str(CurrentElementidentifierforselection)
		print "Click_MultipleUIElements_Selectpassedelement Name===>"+str(CurrentElementnameforselection)
		status = True
				
		try:
												
			elements=[]
			# getting the button element
			elements = self.ui_elements(identifier, tag_name)
			
			print  "printing elements from Click_MultipleUIElements function"
			print elements
			
			for Currentelementtext in elements:
				print Currentelementtext.text
							
			print "Passed element name for selection is==>"+str(Elementnameforselection)
						
						
			for el in elements:
				if el.text.strip()==Elementnameforselection.strip():					
					print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)					
					print "Congratulation!!!Required element has been found successfully,now we can select and click on it"
					print "Reseting global count variable Uipagescrollcount"
					Uipagescrollcount=0
					status=True		
					el.click()																		
					
					break
				else:
					print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)
					print "Passed element has not been found till now trying for more."
					status=False
					continue
			
			'if element passed for selection does not exist on ui at all then return the proper message for failure'
			if status==False:
				print  CurrentElementidentifierforselection
				print CurrentElementnameforselection
				self.swipe_down()
				if Uipagescrollcount==50:
					print "Reached max count 50 can not scroll more"
					print  "Sorry!!!Traversed through entire ui element but not finding passed element for selection,passed element is==>"+str(Elementnameforselection)
					print "Reseting global count variable Uipagescrollcount"
					Uipagescrollcount=0
					print "global count variable Uipagescrollcount value after final reset is====>"+str(Uipagescrollcount)
				else:
					self.Click_MultipleUIElements_Selectpassedelement(get_obj_identifier(CurrentElementidentifierforselection),Elementnameforselection=CurrentElementnameforselection)											
		except:
			traceback.print_exc()
			status = False
		return status	
		
	def hi_Click_MultipleUIElements_Selectpassedelement(self, identifier, tag_name=None,Elementnameforselection=None,elementidentifier=None,elementname=None):

		"""
		This function is used to select an specific element once ui page is returning multiple elements with same resource id.
		Function Owner : Sudhish_Singh
		Date created :
		@param  identifier: (string) object identifier.
		@param  tag_name=None: (string) tag name.
		@param  Elementnameforselection: (string) element name which need to select from multiple elements.		
		@return status : (bool)status of execution.if successful True else False
		"""
		global Uipagescrollcount
		global CurrentElementidentifierforselection
		global CurrentElementnameforselection
		
		#Uipagescrollcount = Uipagescrollcount+1
		#print  "Function call count==>"+str(Uipagescrollcount)
		#if Uipagescrollcount==1:
			#CurrentElementidentifierforselection = elementidentifier
			#CurrentElementnameforselection=elementname
					
		#print "Selectpassedelement identifier===>"+str(CurrentElementidentifierforselection)
		#print "Selectpassedelement Name===>"+str(CurrentElementnameforselection)
		status = True
		#msg, status = "", True
				
		try:
												
			elements=[]
			#getting the button element
			elements = self.ui_elements(identifier, tag_name)
			
			#print  "printing elements from Click_MultipleUIElements function"
			#print elements
			
			#for Currentelementtext in elements:
				#print Currentelementtext.text
							
			print "Passed element name for selection is==>"+str(Elementnameforselection)
						
						
			for el in elements:
				if el.text.strip()==Elementnameforselection.strip():					
					#print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)					
					print "Congratulation!!!Required element has been found successfully,now we can select and click on it"
					print "Reseting global count variable Uipagescrollcount"
					#Uipagescrollcount=0
					status=True	
					el.click()																				
					break
				else:
					#print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)
					#print "Passed element has not been found till now trying for more."
					status=False
					continue
			
			'if element passed for selection does not exist on ui at all then return the proper message for failure'
			if status==False:
				#print  CurrentElementidentifierforselection
				#print CurrentElementnameforselection
				self.swipe_down()
				if Uipagescrollcount==2:
					#print "Reached max count 50 can not scroll more"
					#print  "Sorry!!!Traversed through entire ui element but not finding passed element for selection,passed element is==>"+str(Elementnameforselection)
					#print "Reseting global count variable Uipagescrollcount"
					Uipagescrollcount=0
					#print "global count variable Uipagescrollcount value after final reset is====>"+str(Uipagescrollcount)
				else:
					self.hi_Click_MultipleUIElements_Selectpassedelement(get_obj_identifier(CurrentElementidentifierforselection),Elementnameforselection=CurrentElementnameforselection)											
		except:
			traceback.print_exc()
			status = False
		return status	
		    
                                       



			
	def duplicate_Click_MultipleUIElements_Selectpassedelement(self, identifier, tag_name=None,Elementnameforselection=None,elementidentifier=None,elementname=None):

		"""
		This function is used to select an specific element once ui page is returning multiple elements with same resource id.
		Function Owner : Sudhish_Singh
		Date created :
		@param  identifier: (string) object identifier.
		@param  tag_name=None: (string) tag name.
		@param  Elementnameforselection: (string) element name which need to select from multiple elements.		
		@return status : (bool)status of execution.if successful True else False
		"""
		global Uipagescrollcount
		global CurrentElementidentifierforselection
		global CurrentElementnameforselection
		
		Uipagescrollcount = Uipagescrollcount+1
		print  "Function call count==>"+str(Uipagescrollcount)
		if Uipagescrollcount==1:
			CurrentElementidentifierforselection = elementidentifier
			CurrentElementnameforselection=elementname
					
		print "Click_MultipleUIElements_Selectpassedelement identifier===>"+str(CurrentElementidentifierforselection)
		print "Click_MultipleUIElements_Selectpassedelement Name===>"+str(CurrentElementnameforselection)
		status = True
				
		try:
												
			elements=[]
			# getting the button element
			elements = self.ui_elements(identifier, tag_name)
			
			print  "printing elements from Click_MultipleUIElements function"
			print elements
			
			for Currentelementtext in elements:
				print Currentelementtext.text
							
			print "Passed element name for selection is==>"+str(Elementnameforselection)
						
						
			for el in elements:
				if el.text.strip()==Elementnameforselection.strip():					
					print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)					
					print "Congratulation!!!Required element has been found successfully,now we can select and click on it"
					print "Reseting global count variable Uipagescrollcount"
					Uipagescrollcount=0
					status=True
					el.click()																				
					break
				else:
					print  "Current element is==>"+str(el.text)
					print   "Passed element is==>"+str(Elementnameforselection)
					print "Passed element has not been found till now trying for more."
					status=False
					continue
			
			'if element passed for selection does not exist on ui at all then return the proper message for failure'
			if status==False:
				print  CurrentElementidentifierforselection
				print CurrentElementnameforselection
				self.swipe_down()
				if Uipagescrollcount==2:
					print "Reached max count 50 can not scroll more"
					print  "Sorry!!!Traversed through entire ui element but not finding passed element for selection,passed element is==>"+str(Elementnameforselection)
					print "Reseting global count variable Uipagescrollcount"
					Uipagescrollcount=0
					print "global count variable Uipagescrollcount value after final reset is====>"+str(Uipagescrollcount)
				else:
					self.duplicate_Click_MultipleUIElements_Selectpassedelement(get_obj_identifier(CurrentElementidentifierforselection),Elementnameforselection=CurrentElementnameforselection)											
		except:
			traceback.print_exc()
			status = False
		return status		
			
			

		
	
    