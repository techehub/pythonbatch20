import re

content = "aaaa" \
          "What is your name ? gshdfsd" \
          "sdfsdf dsfdf" \
          "Where is your house ? sdjfhsdf" \
          "sdflsdhfkhsdf" \
          "sdfsdfs" \
          "asdasd How bad product it is !!"


res =re.finditer("(What|Where|Which|How)[\s\w]+(\?|!)+", content)

print (res)

for x in res :
    print (x)

