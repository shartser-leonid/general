def test2(request):
    html1="<script src='https://code.responsivevoice.org/responsivevoice.js'+';'></script>"
    html2="<script>responsiveVoice.speak('Thank you!');</script>" 
    html3="<script>responsiveVoice.speak('Wilokomen!');</script>" 
    return HttpResponse(html1+html2+html3+html2)

def chain_responses(r):
    h=''
    for html in r:
        h += html.content.decode()
    return HttpResponse(h)
