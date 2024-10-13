def OnlyOne():
    aboba = input("ra ginda aba")  

    
    dayofili = list(aboba)  
  
    duplicatebi = len(dayofili) != len(set(dayofili))
    

    print("asoebi meordeba she zango:", duplicatebi)

OnlyOne()