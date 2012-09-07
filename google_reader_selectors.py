'''
Created on 03.08.2012

@author: avkoltsov
'''

class GoogleReaderSelectors(object):
    subscriptions = 'css=#sub-tree .sub.unselectable.expanded'
    entries = 'css=#entries .entry'
    spinner = 'id=activity-indicator'
    loading_area = 'id=loading-area'
    viewer_entries_container = 'id=viewer-entries-container'