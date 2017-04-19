class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=open('result.html','w')
        fout.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href='%s' target='_blank'>%s</a></td>" %(data['url'],data['url']))
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
           # fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()