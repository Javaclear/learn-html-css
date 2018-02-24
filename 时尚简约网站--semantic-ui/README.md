这套模板增加了禁止查看源代码功能，为了练习。实际生产中，建议移除这部分代码。

```

<script type="text/javascript">
 		window.onload = function() {
            document.onkeydown = function() {
                var e = window.event || arguments[0];
                //屏蔽F12
                if(e.keyCode == 123) {
                    return false;
                //屏蔽Ctrl+Shift+I
                } else if((e.ctrlKey) && (e.shiftKey) && (e.keyCode == 73)){
                     return false;
                //屏蔽Shift+F10
                } else if((e.shiftKey) && (e.keyCode == 121)){
                    return false;
                //屏蔽Ctrl+S
                } else if((e.ctrlKey) && (e.keyCode == 83)){
                    return false;
                }
            }
             //屏蔽右键单击
            document.oncontextmenu = function() {
                 return false;
            }
        }
    </script>
    
```


开发过程中使用的图片及视频资源，均来自 https://pixabay.com/ 。
