var docs=document.getElementsByClassName("detail-pop")
for(let i=0;i<docs.length;i++){
    print(docs[i].style)
    var style=docs[i].style
    style.display="block"
}