目標：撰寫程式建構Gaussian Mixture Model，完成color image segmentation。具體而言，就是判別每一個pixel是屬於場地或非場地。

資料：共兩張足球轉播畫面及其對應的場地mask。

需繳交內容：程式原始碼（可使用現成的library）、書面報告。書面報告中須包含1) 程式執行環境及說明、2) 三個scenarios的實驗報告、3) 切割效能以pixel accuracy表示。三種scenarios說明如下：

(1) Scenario 1: 以soccer1.jpg中的場地pixel建構GMM，稱此模型為M1，並以soccer1.jpg做測試

(2) Scenario 2: 以M1針對soccer2.jpg做測試

(3) Scenario 3: 以soccer1.jpg以及soccer2.jpg中的場地pixel建構GMM，稱此模型為M2，並以soccer1.jpg以及soccer2.jpg做測試 



報告中詳述以不同數量mixture建構的GMM的效能差別，以及三種不同scenarios的效能差別



繳交方式：將程式碼及書面報告放在同一目錄，然後整個目錄壓縮成一個zip檔，上傳至moodle

繳交期限：4月12日23:59



https://github.com/Prasheel24/image-segmentation-gmm/blob/master/Code/model_all_colors_3D.py