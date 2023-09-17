package Steganography
import java.io.{File, FileWriter, FileReader}


object SteganographyEncoder {
  val RUS_LETTERS = "аеорсухАВЕКМНОРСТХ"
  val ENG_LETTERS = "aeopcyxABEKMHOPCTX"

  def encode(messagePath: String, containerPath: String, stegocontainerPath: String): Unit = {
    val container = new FileReader(containerPath)
    val fromMessage = new FileReader(messagePath)
    val stegocontainer = new FileWriter(stegocontainerPath)

    var letterToEncode = 0
    var encodedBits = 8
    var isEndOfMessage = false

    try {
      while (true) {

        val symbolFromText = container.read() // считывание символа из текста, который кодируем

        // если файл считан
        if (symbolFromText == -1) {
          return
        }

        var symbolFromTextChar = symbolFromText.toChar

        if (ENG_LETTERS.contains(symbolFromTextChar) || RUS_LETTERS.contains(symbolFromTextChar)) {
          if (encodedBits == 8) {
            // считывание символа из сообщения
//            letterToEncode = fromMessage.read() match {
//              case -1 => // если символ считан
//                if (!isEndOfMessage) {
//                  isEndOfMessage = true
//                  '@'.toInt
//                } else {
//                  '0'.toInt
//                }
//              case c => c
//            }
            letterToEncode = fromMessage.read()
            if (letterToEncode == -1) {
              if (!isEndOfMessage) {
                letterToEncode = '@'
                isEndOfMessage = true
              } else {
                letterToEncode = '0'
              }
            }
            letterToEncode = letterToEncode.toInt
            encodedBits = 0
          }

          val bitFromLetter = (letterToEncode & 0x80) >> 7

          if (bitFromLetter == 1 && ENG_LETTERS.contains(symbolFromTextChar)) {
            val index = ENG_LETTERS.indexOf(symbolFromTextChar)
            val newSymbol = RUS_LETTERS.charAt(index)
            symbolFromTextChar = newSymbol
          } else if (bitFromLetter == 0 && RUS_LETTERS.contains(symbolFromTextChar)) {
            val index = RUS_LETTERS.indexOf(symbolFromTextChar)
            val newSymbol = ENG_LETTERS.charAt(index)
            symbolFromTextChar = newSymbol
          }

          letterToEncode <<= 1
          letterToEncode %= 256
          encodedBits += 1
        }

        stegocontainer.write(symbolFromTextChar)
      }
    } finally {
      container.close()
      fromMessage.close()
      stegocontainer.close()
    }
  }
}
