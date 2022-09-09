import zipfile, re

num = '90052'
f = zipfile.ZipFile('channel.zip','r')

comments=[]
while True:
    content = f.read(num + ".txt").decode("utf-8")
    print(content)
    comments.append(f.getinfo(num+'.txt').comment.decode('utf-8'))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))

#hockey