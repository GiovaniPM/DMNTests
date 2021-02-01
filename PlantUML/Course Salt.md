<div align="center">

![Title](http://satyr.io/1000x80/1?text=Building+Mockups+with+PlantUML)<br>
by [![Email](https://img.shields.io/badge/mail-giovanipm%40gmaill.com-lightgray.svg)](mailto:giovanipm@gmail.com)

</div>

<div align="right">

[![PlantUML 1.2020.23](https://img.shields.io/badge/PlantUML-1.2020.23-brightgreen.svg)](https://plantuml.com/)
[![Creole 1.00](https://img.shields.io/badge/Creole-1.00-brightgreen.svg)](https://web.archive.org/web/20190417093012/http://www.wikicreole.org/wiki/Home)
[![Graphviz 2.44.1.20201124](https://img.shields.io/badge/Graphviz-2.44.1.20201124-brightgreen.svg)](https://graphviz.org/)
<br>Try install using:<br>
[![Chocolatey 0.10.15](https://img.shields.io/badge/Chocolatey-0.10.15-brightgreen.svg)](https://chocolatey.org/install)
<br>To see on Firefox browser:<br>
[![Firefox](https://img.shields.io/badge/Firefox-84.0.2-brightgreen.svg)](https://www.mozilla.org/pt-BR/firefox/new/)
[![PlantUML Visualizer](https://img.shields.io/badge/PlantUML--Visualizer-84.0.2-brightgreen.svg)](https://addons.mozilla.org/en-US/firefox/addon/plantuml-visualizer/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)
[![PlantUML Extension](https://img.shields.io/badge/PlantUML--Extension-84.0.2-brightgreen.svg)](https://addons.mozilla.org/en-US/firefox/addon/plantuml-extension/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)

</div>

# Language specification

## Requeriments

- Light [Creole](https://plantuml.com/creole) engine syntax;
- [Common PlantUML commands](https://plantuml.com/commons);
- [Salt PlantUML standards](https://plantuml.com/salt)
- [Graphviz](https://graphviz.org/)

## Salt Wireframe

### Basic Widget

- **Text**
  create a text representation.
  >_string_
  >- - -
  >ex.:<br>
  >```dos
  >  This is a text
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9G2Cd8B5O0eaI5ajIA4gvQBeVKl1IGB000)

- **Button**
  create a button representation.
  >**[**_string_**]**
  >- - -
  >ex.:<br>
  >```dos
  >  [This is my button]
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GY0x9o2nM0ABSIeMaqfAI_BnOhbekXzIy590I0000)

- **Radio Button**
  create a radio button representation.
  >**()** _string_<br>
  >or<br>
  >**(X)** _string_<br>
  >- - -
  >ex.:<br>
  >```dos
  >  ()  Unchecked radio
  >  (X) Checked radio
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GqD1KK0ZDIyv8JSvEJL4eIap9p0U9HcWgEAE8rN8vfEQbWBG10000)

- **Check Box**
  create a check box representation.
  >**[]** _string_<br>
  >or<br>
  >**[X]** _string_<br>
  >- - -
  >ex.:<br>
  >```dos
  >  []  Unchecked box
  >  [X] Checked box
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GY8vLK0ZDIyv8JSvEJL58ogy0YKN4AZWZYTHoEQJcfO2q0000)

- **Input Box**
  create a input box representation.
  >**"**_string_**"**<br>
  >- - -
  >ex.:<br>
  >```dos
  >  "Enter text here   "
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GK7BDAqajKYX9hIXHo4WjIbK02d7LSZcavgM0r000)

- **Droplist**
  create a input box representation.
  >**^**_string_**^**<br>
  >- - -
  >ex.:<br>
  >```dos
  >  ^This is a droplist^
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GY0l9o2nM0A94XPIY_8ASpEAIEAvQBeVKl1IG6W00)

### Using Grid

Manage colunms to show and organize like a table, in a screen could be used in the aligment of the widgets or even other grids.<br>

- **Grid**
  A table is automatically created when you use an opening bracket **{**. And you have to use **|** to separate columns.<br>
  >**{ | | | }**<br>
  >- - -
  >ex.<br>
  >```dos
  >{
  >  Login    | "MyName   "
  >  Password | "****     "
  >  [Cancel] | [  OK   ]
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GyCbFpynJ088Q1INVIh_4t5GWMmae4P1ON5oUNvG2aj020f0Qi4IqSs9UScfEB50YMa71tnie7CjLo-MGcfS2DXK0)

- **Show Lines**
  Just after the opening bracket, you can use a character to define if you want to draw lines or columns of the grid<br>
  >|Symbol|Result|
  >|:----:|------|
  >|#| To display all vertical and horizontal lines|
  >|!|	To display all vertical lines|
  >|-|	To display all horizontal lines|
  >|+|	To display external lines|
  >- - -
  >ex.<br>
  >```dos
  >{+
  >  Login    | "MyName   "
  >  Password | "****     "
  >  [Cancel] | [  OK   ]
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6grkPIKF39Jy_CKm226WKbtqg_nDnK85i9A16GM5nSdb-K0fBG0WAWC4GYsZanBpar9nOe4QsWuEyD58xbgkLoICrB0HaB0000)

- **Group Box**
  Create a group box representation<br>
  >**{^"**_string_**"** ... **}**<br>
  >- - -
  >ex.<br>
  >```dos
  >{^"My group box"
  >  Login    | "MyName   "
  >  Password | "****     "
  >  [Cancel] | [  OK   ]
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gZbFohLH8ByelBL18ogzGub9GyCbFpynJ088Q1Q2SNs9kAf0DaWX8B2ukpozA0Kbe0G5G628HxPoObvoQ4mkKY5PGyFS62iTorN8vfEQbW2m10000)

- **Scroll Bars**
  You can use {S notation for scroll bar<br>
  >**{S** _..._ **}**<br>
  >|Symbol|Result|
  >|:----:|------|
  >|S| for horizontal and vertical scrollbars|
  >|SI|	for vertical scrollbar only|
  >|S-|	for horizontal scrollbar only|
  >- - -
  >ex.<br>
  >```dos
  >{S
  >  Message
  >  .
  >  .
  >  .
  >  .
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6g3kRoJIqkJanFvTA3mbekXzIy5B0i0000)

- **Line separators**
  You can use several horizontal lines as separator.<br>
  >|Symbol|Result|
  >|:----:|------|
  >|..| Dot line|
  >|==|	Double line|
  >|~~|	Strong line|
  >|--|	Normal line|
  >- - -
  >ex.<br>
  >```dos
  >{
  >  Text1
  >  ..
  >  "Some field"
  >  ==
  >  Note on usage
  >  ~~
  >  Another text
  >  --
  >  [Ok]
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9G24cjA344qdfwG48fE3ytLI4jCpKdHGd8jRK54dxv9QaA-NaAfSM9wQb0VbqTa73Coo_9I2rIA07g1d9rTO54j7zsB5SjbqDgNWhOT000)

- **Tree**
  To have a Tree, you have to start with {T and to use + to denote hierarchy.<br>
  >**{T** ... **}**<br>
  >- - -  
  >ex.<br>
  >```dos
  >{T
  >   + World
  >   ++ America
  >   +++ Canada
  >   +++ USA
  >   ++++ New York
  >   ++++ Boston
  >   +++ Mexico
  >   ++ Europe
  >   +++ Italy
  >   +++ Germany
  >   ++++ Berlin
  >   ++ Africa
  >}
  >``` 

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvgeEuLBGLWZFByf90JAq5HnpKuioanD1R6q5vyIyn1GeEpJO4SpGLl1BBLU8p2_AXdATyejBylCWYdnJApAJyy46kPOMvHUaGeGzIn9pAY5CzzIYtCIyIfZUrAASp3o8nMbWUsk1q24rBmNiF000)

- **Tree table**
 You can combine trees with tables.<br>
  >**{T | | }**<br>
  >- - -  
  >ex.<br>
  >```dos
  >{T
  >  +Region        | Population    | Age
  >  + World        | 7.13 billion  | 30
  >  ++ America     | 964 million   | 30
  >  +++ Canada     | 35 million    | 30
  >  +++ USA        | 319 million   | 30
  >  ++++ NYC       | 8 million     | 30
  >  ++++ Boston    | 617 thousand  | 30
  >  +++ Mexico     | 117 million   | 30
  >  ++ Europe      | 601 million   | 30
  >  +++ Italy      | 61 million    | 30
  >  +++ Germany    | 82 million    | 30
  >  ++++ Berlin    | 3 million     | 30
  >  ++ Africa      | 1 billion     | 30
  >}
  >```
  >or
  >```dos
  >{
  >  ..
  >  == with T!
  >  {T!
  >  +Region        | Population    | Age
  >  + World        | 7.13 billion  | 30
  >  ++ America     | 964 million   | 30
  >  }
  >  ..
  >  == with T-
  >  {T-
  >    +Region        | Population    | Age
  >    + World        | 7.13 billion  | 30
  >    ++ America     | 964 million   | 30
  >  }
  >  ..
  >  == with T+
  >  {T+
  >    +Region        | Population    | Age
  >    + World        | 7.13 billion  | 30
  >    ++ America     | 964 million   | 30
  >  }
  >  ..
  >  == with T#
  >  {T#
  >    +Region        | Population    | Age
  >    + World        | 7.13 billion  | 30
  >    ++ America     | 964 million   | 30
  >  }
  >  ..
  >}
  >```

  ![example](http://www.plantuml.com/plantuml/png/RT5BYy8m403WUtx5t0FIMBVgpIeYUzXbyO5u7Dki6qYJagQmOltlLadQWabkmvTvP1QLHMChb9RSo6rFw9PVX5RWJWC_kgmbMXTh8BrmGk6eZSnxD1sn6Cv2oXTh88u8fP0Mt8WCdPad4oWyyOR22XNctiGV0zARmoxjQyLi7iX3uVkqwinic6PWbhgoFdV2fc3_T5sXoWUrllY_oBHxnrhpLWlMjT4bzxMIY8Nc-hGehvrXmRast1IehgxdSSYqFNCZXO-5veBqj_lcPy_z8hovjtV1LVvQymC0)
  <br>or<br>
  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvjBJuxArLIZFBCbG257agWPYxQ3KzCpyF0Keg548o2yepKaiWOhLA3Ycft9fAuJd5-Ma81IPwnaQAoHbvkI0bTKe61jmQMihEEQc5cKc9qBLM9gPAEJ2b43KrA8uG1Ve0Ds1T80sq07Q0-a0PQ03b0V00RLS3gbvAU0q0G00)

- **Advanced table**
  >**{# | | }**<br>
  >|Symbol|Result|
  >|:----:|------|
  >|*| to indicate that a cell with span with left|
  >|.| to denotate an empty cell|
  >- - -  
  >ex.<br>
  >```dos
  >{#
  >  . | Column 2 | Column 3
  >  Row header 1 | value 1 | value 2
  >  Row header 2 | A long cell | *
  >}
  >``` 

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gLkRIKwXHSCxFAStDKp12C8svWlBB5J9I4rDIYnGCWU9bYJcbgKWi8sG588sE2ZdvUUaAoQavEK2U5bSjbqDgNWhO5W00)

- **Enclosing brackets**
  You can define subelements by opening a new opening bracket.<br>
  >**{# | { | | } | }**<br>
  >- - -  
  >ex.<br>
  >```dos
  >{
  >  Name         | "                 "
  >  Modifiers:   | { (X) public | () default | () private | () protected
  >                  [] abstract | [] final   | [] static }
  >  Superclass:  | { "java.lang.Object " | [Browse...] }
  >}
  >``` 

  ![example](http://www.plantuml.com/plantuml/png/NOyz3eCm38NtdC9YWYK7w8IwjnswLAeOJ6Age1HGOkX0kNkTL2oyxPFyVbn7ni0HFQjLNV5DiEiB1HnLgCjeNUSen5C-MQ5yL33DhNT6iAp0KeUpvpzCmIt8jCF8P9YiEiO-6y0sSa2JV4AT6z3d0W5Po9A-gViyKJ0UOofFtKMF2sgFmqlVsbwoPR9Opc7yHD9QDsBQL4s3pG_-0000)

### Adding tabs

- **Tabs**
  You can add tabs using {/ notation. Note that you can use HTML code to have bold text.<br>
  >**{/ | | }**
  >- - -
  >ex.<br>
  >```dos
  >{+
  >  {/ <b>General | Fullscreen | Behavior | Saving }
  >  {
  >    { Open image in: | ^Smart Mode^ }
  >    [X] Smooth images when zoomed
  >    [X] Confirm image deletion
  >    [ ] Show hidden images
  >  }
  >  [Close]
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/DOwn2W8n44JxVCNs5lOYSdYWbLYa4OuxY6Qz199TIQ87Hl_TvTHkbZSpEqqk9fLiGb5reUeIrkVD7WcJ2V22tJs4V4c89CSMdNbuJYAr21hXhQggSBm9zj6C29vMGWSTfHCER74GJtVgGKVcuhwk39EJn9CvefrfotJrAVvAB0Oidabr84774pXlxVz7LjBO1ixOYsgGx3p-0m00)

- **Vertical Tabs**
  You can add tabs using {/ notation. Note that you can use HTML code to have bold text.<br>
  >**{/<br>
  >  ...<br>
  >  ...<br>
  >} |**
  >- - -
  >ex.<br>
  >```dos
  >{+
  >  {/ <b>General
  >     Fullscreen
  >     Behavior
  >     Saving } |
  >  {
  >    { Open image in: | ^Smart Mode^ }
  >    [X] Smooth images when zoomed
  >    [X] Confirm image deletion
  >    [ ] Show hidden images
  >  }
  >  [Close]
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/DKuz2y8m4DtlLzpku2uYnO9Euj15A2r4SpQ1v4wIQC6q_zrGbJUyuNrMCQcGed89yWho6hVNtP6OWd9mU3eNRu68OKz6lQm4Q0hnW3DEa27Z-K6Crgk1qF869-mRN_hm99fwdA6zTDXuaMI-heYZAOctY2UzgBNmtGR_Az7aA5bXQB44ZOnehDR_ZGXjxIHI1tD1HQoNuny0)

### Using menu

- **Menus**
  You can add a menu by using {* notation. 
  >**{\* | | }**
  >- - -
  >ex.<br>
  >```dos
  >{+
  >  {* File | Edit | Source | Refactor }
  >  {
  >    { Open image in: | ^Smart Mode^ }
  >    [X] Smooth images when zoomed
  >    [X] Confirm image deletion
  >    [ ] Show hidden images
  >  }
  >  [Close]
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/BOx12i8m38RlVOgSzGqy3ORUH70NOMnGrim6saRQoC3gkvlfJadu_-yZJH6RfTWWfkvDtS690i8RZev4HyVFFAtt5MSx2MVuc6egN1wOWAAz8r0wQ3vsKJrmPeUZTlhR05ra5lzl5LYy4Y_cYEwNjfncod6JE0menCdqeA3d1JmvXscZZHhRm0K7tHfCRdtu2m00)

- **Open Menus**
  >**{\* | | }**
  >- - -
  >ex.<br>
  >```dos
  >{+
  >  {* File | Edit | Source | Refactor
  >     File | New | Open File | - | Close | Close All }
  >  {
  >    { Open image in: | ^Smart Mode^ }
  >    [X] Smooth images when zoomed
  >    [X] Confirm image deletion
  >    [ ] Show hidden images
  >  }
  >  [Close]
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/FOzFYyCW4CNlVeevxx9VO4zPmlRM5ffB8IGWSL85TOfE2TJsktUID3teyy_llQTLPfquQy-gVAlo1Jld4HxmRnoBD7HBmxm_uQW7fgGsu82JpCShnktaHqRjAUD7_xo7foggh9mB-eBWugy0VHEa5_Pai1UcFNVG12AsAvLXikAu4mKqosrDSNGfl4CCUcH7KRKWHaiJM6VCrf6L92vFw6HLOJJp1ry0)

### OpenIconic

- **OpenIconic**
  OpenIconic is a very nice open source icon set. Those icons have been integrated into the creole parser, so you can use them out-of-the-box. You can use the following syntax: <&ICON_NAME>.<br>
  ```plantuml
    @startuml
    listopeniconic
    @enduml
  ```
  >**<**_icon name_**>**
  >- - -
  >ex.<br>
  >```dos
  >{
  >  Login<&person> | "MyName   "
  >  Password<&key> | "****     "
  >  [Cancel <&circle-x>] | [OK <&account-login>]
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU6gvb9GyCbFpyopKIj8BIhEpxDJg55GygtqIynDLL1GK09A1oGM5vVd5wNOg6MdLeAbjO10GG4g7UsSc9UScgDWevQSMPISawfROHSBL1JjxmqKIanEpY_DAz7D0LbX5yjLo-MGcfS2jXa0)

### Pseudo sprite

- **Pseudo sprite**
  Using << and >> you can define a pseudo-sprite or sprite-like drawing and reusing it latter. <br>
  >**<<**_sprite name_<br>
  >  ............<br>
  >  .XXXXX......<br>
  >  .X...X......<br>
  >  .XXXXXXXXXX.<br>
  >  .X........X.<br>
  >  .X........X.<br>
  >  .X........X.<br>
  >  .X........X.<br>
  >  .XXXXXXXXXX.<br>
  >  ............<br>
  >  **>>**<br>
  >- - -
  >ex.<br>
  >```dos
  >{
  >  <<folder
  >    ............
  >    .XXXXX......
  >    .X...X......
  >    .XXXXXXXXXX.
  >    .X........X.
  >    .X........X.
  >    .X........X.
  >    .X........X.
  >    .XXXXXXXXXX.
  >    ............
  >  >>
  >  reusing
  >  <<folder>>
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAKxCAU5IgEPIiB59oyz9IItYKj130a1U10WWU40AYGS743ae89M7C0NTTZixBeMYrDBYpBnqX1E1WhLS3gbvAI370m00)

- **Convert image to sprite**
  How convert a image to sprite.<br>
  1. Get some image
  2. Reduce to  the color to **B/W**
  3. Change the resolution: horizontal to **50%** and stay with vertical in **100%**
  4. Change the file resolution at maximun in **500 Kb** size
  5. Go to website [Convert Images to Ascii Art](https://manytools.org/hacker-tools/convert-images-to-ascii-art "Convert Images to Ascii Art")
  6. Click the button **Browse...** and select your image
  7. In **Width of output (in characters, max 200)** put 200
  8. Click in the button **Convert!**
  9. Click in the button **Download ASCII (.TXT)**
  10. Open the downloaded file
  11. Replace all different character of space (!@#$%^&*()_+-=/\,.:;) by **X** (x in uppercase)
  12. Replace all space character to **.** (point)
  13. Save the downloaded file
  14. Get the content of downloaded file, and use as content in your sprite definition

  Ex.:
  ||||
  |:----:|:----:|:----:|
  | ![example](http://www.plantuml.com/plantuml/png/xTrHYXj74CRnzpw5Jr0dCCR7gDU5c11m4l3kMyZTys86zaEb_topLMuXKWz1JAQhwkTMhuH6q_hw-lRou-trvVlR-lJF-lJvy-y_lltvnzyhXYD_HWp732JlnnXadZ3FMIE63PhLhzXZMKC8__JTaCijDLjMfs9-_0oafuacoXgkxvwKyn2dTDwFVWj3YE4QperiXm233H2SUWu2NMoZh2w6Bw4iFH1mw46V8gDyYWT1XXwo6982A0qGBiWKOXIPco30a0Yoy9a-XI7aAFe32wN8gvBLm2WiG8tpq3R8MKPHjJXeFFEQ8FuIeB0NKGS46201Hz-ah6678G6A0G570yEIf2LPOmw8PWb0V0Oxh6pd9MlGqV_qOiYyOrgoJZgotn7P8m58ieCXBP9a2KD67QsIjTFHALaTZdw8BrbR7OsIjTVH9rbTZca8ITPcHvk48F4ma70XUkAWmozGInOv8Xu24W6ITSTXB9I88KdT3qDkV2RhGjwDU_z8pZUoQpjt8JeG9LLVyiPJ7ZYGkXs1L0vfqe147928p7p_A28SYTHNIGrHXnuWo27usM--rqGO42ckhXfIzKtrmeFe2CvSoMg8Ea3YGb8kwm0aecwcXgYZfZ145xj2aY5QaoGBdrZIB3lqpo-laO3fi27guCm0YOXJaE1Y95au8PmT8FpdDy9X4AHmq2MpeYbP3ySX65CpIB9qGgnhC03HelLxrxe2GL8WKhJrSbB3HJ6UakLDY5RhWm13euIeyombkY26Gbgj87akOYAC-WL4b1ieo80fKKYa4-CA0m8JWh53eV_iFcJCShbg2SbhqQ_W48Wn8H23282aG21ljwQdr1I4EBrL1AA-_U5FYK3Qopm1969UygmGcQQ-6ZaeaQO5qbiZSr8YNKz1Zlnx8EsEVWb1fbVc_29PaSy7gKvyb8xl7gyXrdr3-3Qh_iHA3jCjLox4lq7bAYHAI97FWbovC_qy9002jUv0ZET73Obs24m-GwhE0H9N8747WXz40gI0utAaLoJjcI0rMrej815sgmOaRKWMZGX4PgWOJwtw43scaA8FFLf3Yl7P1icFGTA65D432OR0rKM6aACVaXOa9o5XGEIY8a3obqBu1L4X4UEGO4WH-KiXOKESrsu38aVsGyI147dG1uac27vreXy2Rr4kG-8Q9Az1qeCKRSW99kG014E28P4Ln7-BSWKI5o5n3v8F2CcFGaHYGCA4QFV-kr-2sAswa8mZ418N8BKaDa2WZvCGSHkG8Wf85X0vgtO815wTso4946X48UMdyJS7Ru0KsPpB2ZV6xe1anG18ASaQ8X8FaWJ9h1aCqHIv9RYHg23REzv_URe__eSymtTH9h-CeZ4r8HEGE1FJaEWdZ6cYW1p0ViICPk3BcV7H6814lsB84WeHIRzYo49VAOz-nGWb2eWWkndz5hxj8an6ZoXDIdH0f6WBHD8Q4o8GaXICHWXGO49yY9HgafJvVOXAaD4D0GeuJ8YMw8Te6LuX2b49Cmg8tWMgDM_AeHHF24CuDq1Ixtgz0O5oXQE0WAJ8gnAzILh_4pe0ixgtWOlHOBYGA25CqGRxjae0oD4zG1o9EYg8If2X4baP1-dGPDOEfjIxS8047G3HH-LE2I1HHmrHA3EEu3KYUHYYoM-uWY1PeL1YGhpaHMi2AIHGoOOSppG3KlLZxA_53fKe9ANpp128axvq2AIOjlmO93eWMNK84F_QoFoD-3BW-NS5B2Jza7w7GlP8EXm06PQOsS7n-9koIYicHEI-fD_1s-JsI-RdWo4icOUmWo7zadu7G-ObWuvONAXVCl534Qlv9o9oti6GUScS8zRqpwZq_vGAGA1WiwHvEgP-esTeEW2oGTBYy26HGF4KGpiFhkxD1s53J2y5Cm32anAaEDyc_l_X7wqBVaQWXHdi88XFGGMVN9JhXKHHpc001MhrGEhqr_SyqWJ0Q8401Hb08KO_XBV7yC8h090kIbu9Wz4AuPiQZA2y_H2a-1Z8sGi12jHb0QJp8JsMpObMLmUPyoa8qcV9_h5p45uC_MD68Rom_HEtG_g_L3yAuPWr0AGz-Wrx8E29eLYVldnP_wwlt_xwxVNb-zj_) | ![example](http://www.plantuml.com/plantuml/png/xTb1QeDG58NX-LlCNK48MSQP2ktCXbBjg7Jl9SKA9d_XoSiHbFkFmY6F3n8HmSimTX_ZqFLZ-IgdqtlVNSVFjxx41YMIo0uHQHD4YPYG1iED212l4SLep58n6HFXGdHhWgm8N5qcmuY0iND4Hq3alwqO4L2iIFWGW7R-IAHRNaHpDaIBF8ZksmJHGP08En9XHwOXaKGumVIugG7HRxpniXhHNxI9btM85k78IpsYXs2ZgX4rLONeYJ4YoOXK68aa4hG1qO305_4ffG7vzyu6GZs2Xs4Z0X1My31iQ01239-jc01XXN_swTDoYRZxmnYP8mEEqrAFHBWGOEn8L20LLm0ZpCJw2C4C26L0A0F2J6C7UQULI2BdS_akbzVhoz3rumy0) | ![example](http://www.plantuml.com/plantuml/png/xTan3e9048NXVW_pJa08ntWjKJkr43hZtOrkOYZ0u6RUkEByrNPVmuRCR3UC_MKS-kEOhgbfJlqk8KT9oAKiw496gEs9KDvs42Rw8Z1k1e4WJoGGacg4r2FK8wGV0WS4GcHg212-cXnj4IvbYF1DvKWv8K1G8I8m0fb1ukkgwJBcZ12u8FWoKkV_f421AGAZ6x-IcHxj4O0nEcmCqK-_-WBH8W3K278k20BvUGGbIftRLBdYjqPNCa16zFqZmhbi4IxaWj0GuHea4Awl5E5d5I4CPDE8A7-aRTCjTOVp_l5AVmS0) |
  ||||

## Using Salt with other graphs in PlantUML

- **salt**
  Could be used in other graphs, using the command salt.
  > **{{ salt {**<br>
  > ..<br>
  > **}**<br>
  > **}}**<br>
  >- - -
  >ex.<br>
  >```dos
  >{
  >  @startuml
  >  rectangle r as "
  >    Text as top
  >    ..
  >    {{
  >      salt
  >      {
  >        {T+
  >          <&folder>Folder1
  >        }
  >      }
  >    }}
  >  "
  >  @enduml
  >}
  >```  

  ![example](http://www.plantuml.com/plantuml/png/SoWkIImgAStDuIfAJIv9p4lFILKeKaWiLb3YKb08IQqe0R5ByWk0F3qz855TpQK01CM9EILW1eWBfaEqWIm8i55Boyz9IIsoSmDJXb29MYuOMLlBfSJba9gN0hGN0000)
  <br>or<br>
  ```plantuml
  @startuml
  foo->Bar
  legend left
  {{
  salt
  {
    Login    | "MyName   "
    Password | "****     "
    [Cancel] | [  OK   ]
  }
  }}
  end legend
  @enduml
  ```
  <br>or<br>
  ```plantuml
  @startuml
  class foo
  note left
  {{
  salt
  {
    Login    | "MyName   "
    Password | "****     "
    [Cancel] | [  OK   ]
  }
  }}
  end note
  @enduml
  ```

## Example

```plantuml
@startsalt
'skinparam BackgroundColor lightblue
scale 1.5
{+
    |area1|area2|area3|area4|area5|area6|area7
    |.|{* File | Edit | Source | ?
    '  File | New | Open File | - | Close | Close All | - | Exit
      ? | About}|*|*|*|*
    |.
    |.|{/ <b>General | Fullscreen | Behavior | Saving }|*|*|*|*
    |.
    |.|Login    |"MyName          "|.
    |.|Password |"****            "|.
    |.
    |.|Open image in|{ ^Smart Mode^ }|{^Options
                                        [X] Smooth images when zoomed
                                        [X] Confirm image deletion
                                        [ ] Show hidden images
                                       }
    |.|Sexo|{(X) Masculino
             () Feminino}
    |.
    |.|Estado|{SI 
                Acre
                Amapa
                Amazonas
              }|{^"Privacy" | (X) public | () default | () private} |*|*
    |.
    |.|{#
        .     | Column 2  | Column 3 | Column 4 | Column 5
        Row 1 | value 1   | value 2  | value 3  | value 4
        Row 2 | long cell | *        | *        | *
       }|*|*|{+{T
              + World
              ++ Europe
              +++ Italy
              +++ Germany
              ++++ Berlin
              ++ Africa
             }}|*
    |.
    |.|.|.|.|[  OK<&account-login>   ]|[Cancel<&circle-x>]
    |.
}
@endsalt
```