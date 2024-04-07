from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

if __name__ == "__main__":
    
    lang_db = {
        "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", 
        "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs", 
        "Bulgarian": "bg", "Catalan": "ca", "Cebuano": "ceb", "Chinese": "zh-TW", "Corsican": "co", 
        "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "English": "en", "Esperanto": "eo", 
        "Estonian": "et", "Finnish": "fi", "French": "fr", "Frisian": "fy", "Galician": "gl", "Georgian": "ka", 
        "German": "de", "Greek": "el", "Gujarati":"gu", "Haitian Creole":"ht", "Hausa":"ha", "Hawaiian":"haw", 
        "Hebrew":"he", "Hindi":"hi", "Hmong":"hmn", "Hungarian":"hu", "Icelandic":"is", "Igbo": "ig", 
        "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jv", "Kannada": "kn", 
        "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kurdish": "ku", "Kyrgyz": "ky", 
        "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb"
    }
    
    select_lang = input("Enter source language: ")
    lang_selection = lang_db.get(select_lang)
    
    if lang_selection is None:
        print("Source language not found.")
    else:
        select_convo = input("Enter target language: ")
        lang_convert = lang_db.get(select_convo)
        
        if lang_convert is None:
            print("Target language not found.")
        else:
            text_to_translate = input("Enter the text to translate: ")
            translated_text = translate_text(text_to_translate, lang_selection, lang_convert)
            print("Translated Text:", translated_text)
