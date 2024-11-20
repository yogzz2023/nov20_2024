I understand you want to ensure the plots appear properly within their respective tabs and containers. Here's what needs to be modified in your code for proper plot integration:

1. For the main plot tab changes, find the `plot_tab` setup section and modify it to:

```python
# Plot Setup
self.plot_tab.setLayout(QVBoxLayout())
plot_container = QFrame()
plot_container.setFrameStyle(QFrame.Box | QFrame.Plain)
plot_container.setLineWidth(1)
plot_layout = QVBoxLayout()
plot_container.setLayout(plot_layout)
plot_layout.addWidget(self.plot_widget)
self.plot_tab.layout().addWidget(plot_container)
```

2. For the search plot and track plot tabs, modify the setup to:

```python
# Add Search Plot and Track Plot tabs
self.search_plot_tab = QWidget()
self.track_plot_tab = QWidget()
self.plot_type_tabs.addTab(self.search_plot_tab, "Search Plot")
self.plot_type_tabs.addTab(self.track_plot_tab, "Track Plot")

# Set up layouts for sub-tabs
self.search_plot_layout = QVBoxLayout()
self.track_plot_layout = QVBoxLayout()
self.search_plot_tab.setLayout(self.search_plot_layout)
self.track_plot_tab.setLayout(self.track_plot_layout)

# Create containers for plot widgets
search_plot_container = QFrame()
search_plot_container.setFrameStyle(QFrame.Box | QFrame.Plain)
search_plot_container.setLineWidth(1)
track_plot_container = QFrame()
track_plot_container.setFrameStyle(QFrame.Box | QFrame.Plain)
track_plot_container.setLineWidth(1)

# Add plot widgets to containers
search_plot_layout = QVBoxLayout()
track_plot_layout = QVBoxLayout()
search_plot_container.setLayout(search_plot_layout)
track_plot_container.setLayout(track_plot_layout)

self.search_plot_widget = pg.GraphicsLayoutWidget()
self.track_plot_widget = pg.GraphicsLayoutWidget()
search_plot_layout.addWidget(self.search_plot_widget)
track_plot_layout.addWidget(self.track_plot_widget)

# Add containers to tab layouts
self.search_plot_layout.addWidget(search_plot_container)
self.track_plot_layout.addWidget(track_plot_container)
```

3. Add some styling for the plot containers:

```python
# Add to the stylesheet
self.setStyleSheet("""
    QFrame {
        background-color: #333333;
        border: 1px solid #555555;
        border-radius: 4px;
    }
    """ + self.styleSheet())
```


1. The complete updated code
2. Just the relevant modified sections
3. Specific sections you're most interested in

Let me know which option you prefer and I'll provide the appropriate response.