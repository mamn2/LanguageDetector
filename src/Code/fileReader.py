import re

def readTrainingFile(file, lang):

    with open(file, 'r') as file:

        data = file.read().replace('\n', '').lower()
        data = data.replace(' ,', '')
        data = data.replace(' .', '')
        data = data.replace(' :', '')
        data = data.replace(' ;', '')
        data = data.replace('( ', '')
        data = data.replace(' )', '')
        data = data.replace(' ?', '')
        data = data.replace(' !', '')
        data = data.replace(' / ', '')

        if lang == "fra":
            data = data.replace('j \' ', 'j\'' )
            data = data.replace('s \' ', 's\'' )
            data = data.replace(' \' - ', '\'')
            data = data.replace('\'- ', '\'')
            data = data.replace('l \' ', 'l\'' )
            data = data.replace('qu \' ', 'qu\'' )
            data = data.replace(' d \' ', ' d\'' )
            data = data.replace(' m \' ', ' m\'' )
            data = data.replace(' n \' ', ' n\'' )
            data = data.replace(' c \' ', ' c\'' )

        if lang == "ital":
            data = data.replace('l \' ', 'l\'' )
            data = data.replace('d \' ', 'd\'' )
            data = data.replace('un \' ', 'un\'' )
            data = data.replace('Un \' ', 'un\'' )
            data = data.replace('dev \' ', 'dev\'' )
            data = data.replace('o \'', 'o\'' )
            data = data.replace('e \' ', 'e\'' )
            data = data.replace('anch \' ', 'anch\'' )
            data = data.replace('quest \' ', 'quest\'' )

        data = data.replace(' - ', '-')
        data = re.sub('\"\s(.{1,80})\s\"', '\"\\1\"', data) # clean weird " " formatting errors

        return data

def readTestFile():

    with open('../Data/Validation/LangId.test', 'r') as file:
        
        lines = []

        for line in file.readlines():
            
            data = line.replace('\n', '').lower()
            data = data.replace(' ,', '')
            data = data.replace(' .', '')
            data = data.replace(' :', '')
            data = data.replace(' ;', '')
            data = data.replace('( ', '')
            data = data.replace(' )', '')
            data = data.replace(' ?', '')
            data = data.replace(' !', '')
            data = data.replace(' / ', ' ')
            data = data.replace('j \' ', 'j\'' )
            data = data.replace('s \' ', 's\'' )
            data = data.replace(' \' - ', '\'')
            data = data.replace('\'- ', '\'')
            data = data.replace('l \' ', 'l\'' )
            data = data.replace('L \' ', 'L\'' )
            data = data.replace('qu \' ', 'qu\'' )
            data = data.replace(' d \' ', ' d\'' )
            data = data.replace(' m \' ', ' m\'' )
            data = data.replace(' n \' ', ' n\'' )
            data = data.replace(' c \' ', ' c\'' )
            data = data.replace('l \' ', 'l\'' )
            data = data.replace('d \' ', 'd\'' )
            data = data.replace('un \' ', 'un\'' )
            data = data.replace('Un \' ', 'un\'' )
            data = data.replace('dev \' ', 'dev\'' )
            data = data.replace('o \'', 'o\'' )
            data = data.replace('e \' ', 'e\'' )
            data = data.replace('anch \' ', 'anch\'' )
            data = data.replace('quest \' ', 'quest\'' )
            data = data.replace(' - ', '-')
            data = re.sub('\"\s(.{1,80})\s\"', '\"\\1\"', data) # clean weird " " formatting errors
            
            lines.append(line)
        
        return lines

#print(readTrainingFile('../Data/Input/LangId.train.English', "eng"))