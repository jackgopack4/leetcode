# 68. Text Justification
import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # First idea, two phase approach
        # Assign words to lines (list of lists of strings) 
        # Then, loop through each list and assign spaces from left to right
        # keeping in mind last line left-justified
        wordLines = [[]]
        lineSpacesNeeded = []
        currentLineCharCount = 0
        currentLine = 0
        for word in words:
            if len(wordLines[currentLine]) > 0:
                currentLineCharCount += 1 # need to add at least one space before word
            
            if maxWidth-currentLineCharCount < len(word):
                lineSpacesNeeded.append(maxWidth - sum([len(w) for w in wordLines[currentLine]]))
                currentLine += 1
                wordLines.append([])
                currentLineCharCount = 0
            currentLineCharCount += len(word)
            wordLines[currentLine].append(word)
        lineSpacesNeeded.append(maxWidth - sum([len(w) for w in wordLines[currentLine]]))
        #print(wordLines)
        #print(lineSpacesNeeded)
        
        # number of breaks between words that need spaces is length of line - 1
        # check if exact division, else round up and subtract until remaining
        # number of breaks is equal to integer number of spaces
        res = []
        for i, (wordLine, spacesNeeded) in enumerate(zip(wordLines,lineSpacesNeeded)):
            numBreaks = len(wordLine) - 1
            if i == len(wordLines) - 1 or numBreaks == 0:
                tmpStr = " ".join(wordLine)
                res.append(tmpStr.ljust(maxWidth))
            else:
                numBreaks = len(wordLine) - 1
                avgNumSpaces = spacesNeeded / numBreaks # will be a float/double
                remainingSpaces = spacesNeeded
                remainingBreaks = numBreaks
                tmpStr = ""
                for word in wordLine:
                    if len(tmpStr) > 0:
                        if remainingSpaces % math.floor(avgNumSpaces) == 0 and \
                            remainingSpaces / math.floor(avgNumSpaces) == remainingBreaks:
                            numSpaces = math.floor(avgNumSpaces)
                        else:
                            numSpaces = math.ceil(avgNumSpaces)
                        tmpStr = tmpStr.ljust(len(tmpStr)+numSpaces)
                        remainingBreaks -= 1
                        remainingSpaces -= numSpaces
                    tmpStr += word
                res.append(tmpStr)

        return res
