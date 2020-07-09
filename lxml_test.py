from lxml import etree


text = """
<div>
    <ul>
        <li class="item-1">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a>
        </li>
    </ul>
</div>
"""

# 创建Element对象
html = etree.HTML(text)

print(html.xpath('//a[@href="link1.html"]/text()'))
print(html.xpath('//a[@href="link1.html"]/text()')[0])

text_list = html.xpath('//a/text()')
link_list = html.xpath('//a/@href')

print(text_list)
print(link_list)

el_list = html.xpath("//a")

for el in el_list:
    print(el.xpath("./text()")[0], el.xpath('./@href')[0])