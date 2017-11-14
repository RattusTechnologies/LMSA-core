"""
Contains functionality not currently bound to any specific operations
"""

import time

class Logic(object):

    def __init__ (self, driver):
        self.driver = driver

    def check_state(self, xpath):
        """Checks the state of a given element, returns
        its boolean value.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        Returns
        -------
        boolean
            Returns 'True' if element is selected, and 'False' otherwise
        """
        x = self.driver.find_element_by_xpath(xpath)
        if x.is_selected() == True:
            return True
        return False

    def set_state(self, xpath, dstate):
        """Sets the desired state of an element.

        Parameters
        ----------
        xpath : str
            Raw xpath formatted as string value. Should be using
            global variable from assignment_options/test_options

        state : bool
            The user's desired state for the given element

        Returns
        -------
        """
        if self.check_state(xpath) != dstate:
            self.driver.find_element_by_xpath(xpath).click()

    def cancel(self, wait=None):
        """Click cancel
        """
        try:
            self.driver.find_element_by_xpath(BB_Editor.CANCEL).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

    def submit(self, wait=None):
        """Click submit
        """
        try:
            self.driver.find_element_by_xpath(BB_Editor.SUBMIT).click()
            if wait is not None:
                time.sleep(wait)
        except:
            return False

class Window(object):

    def __init__ (self, driver):
        self.driver = driver

    def home(self, wait=None):
        self.driver.get('https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1')
        if wait is not None:
            time.sleep(wait)

    def scroll_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_into_view(self):
        self.driver.execute_script("document.getElementById('newFile_chooseLocalFile').scrollIntoView(true);")

    def maximize_window(self):
        self.driver.maximize_window()
