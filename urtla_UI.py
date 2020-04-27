import PySimpleGUI as sg
from PIL import Image, ImageTk
import io
import os
import Learning
import Detect

#ネットから持ってきた画像読み込み関数
def get_img_data(f, maxsize=(450, 300), first=False):
    """Generate image data using PIL
    """
    print("open file:", f)
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:  # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
        
#LearningFrameの設定をする
def get_LearningFrame():
    #データセットを参照するウィジェットの設定
    read_dataset_widget = [sg.InputText("データセットを選択",key = "-INPUT_DATASET-",enable_events=True,),
                        sg.FolderBrowse("読み込み",key = "-LFILE-",)]

    #モデル名を決めるウィジェットの設定
    input_modelName_widget = [sg.InputText("モデル名を入力",key = "-INPUT_MODELNAME-",enable_events = True,),
                            sg.Button('学習')]

    #Learningフレームの設定
    Learnig_frame = [sg.Frame('Learnig',layout = [
                        read_dataset_widget,
                        input_modelName_widget
    ])]

    return Learnig_frame

#ImageFrameの設定をする
def get_DetectFrame():
    #対象画像を参照するウィジェットの設定
    read_image_widget = [sg.InputText("画像を選択",key = "-INPUT_IMAGE-",enable_events=True,),
                        sg.FileBrowse("読み込み",key = "-DFILE-",
                        file_types = (("jpegファイル", "*.jpg"),('png',"*.png"),)),
                        sg.Button("プレビュ")]

    #モデルを参照するウィジェットの設定
    read_model_widget = [sg.InputText("学習モデルを選択",key = "-INPUT_MODEL-",enable_events=True,),
                        sg.FileBrowse("ファイルを読み込む",key = "-FILE-",
                        file_types = (("txtファイル", "*.txt"),))]

    #画像を表示するウィジェットの設定
        
    sample_path = r"C:\Users\gsnow\python_UI計画\Learning.png"
    sample_path2 = r"C:\Users\gsnow\python_UI計画\Detect.png"
    sample_img_elem = sg.Image(data = get_img_data(sample_path,first = True))
    sample_img_elem2 = sg.Image(data = get_img_data(sample_path2,first = True))
    sub_image_frame = [sg.Frame('Image',layout = [[sample_img_elem, sample_img_elem2]])]

    #検出と保存ボタンの設定
    Button_widget = [sg.Button("欠陥検知"),
                    sg.Button("結果保存")]

    #フレームの設定
    Detect_frame = [sg.Frame('Detect',layout = [
                        read_image_widget,
                        read_model_widget,
                        sub_image_frame,
                        Button_widget
    ])]

    return Detect_frame

#プレビュ関数
def Preview():
    print("Preview")
    pass

#右側の画像を保存する
def SaveResult():
    print("SaveResult")
    pass

if __name__ == "__main__":
    #GUIの大元のテーマ
    sg.theme("Dark Blue 3")

    layout = [
        [sg.Text('Learning : 深層学習によるモデル生成   Detect : ニューラルネットを使った画像欠陥検知')],
        [sg.Text('データセットフォルダの中には教師ラベルと訓練画像を用意してください。フォルダ階層は下記の画像を参考にしてください')],
        [sg.Text('Detectする場合、左の画像がオリジナル画像で右の画像が欠陥検知の結果を図示した画像となります')],
        get_LearningFrame(),
        get_DetectFrame()
    ]

    window = sg.Window('深層学習による画像欠陥検知',layout)

    while True:
        event,values = window.read()
        print(event)

        if event is None:
            print("exit")
            break

        if event == "学習":
            Learning.Learning()
        if event == "プレビュ":
            Preview()
        if event == "欠陥検知":
            result_img = Detect.Detect()
            #右側の画像の表示をアップデートする処理
        if event == "結果保存":
            SaveResult()
            #保存完了というボップアップを出す        

    window.close()