```python
import httplib2

h = httplib2.Http('.cache')
response, content = h.request(img)
out = open('...\img.jpg', 'wb')
out.write(content)
out.close()
```