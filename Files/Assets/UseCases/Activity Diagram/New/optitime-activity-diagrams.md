<div dir="rtl">

> **الوثيقة:** مخططات النشاط للحالات الأساسية (Activity Diagrams) — **النظام:** OptiTime — **التاريخ:** 2026-11-08

# مخططات النشاط للحالات الأساسية — نظام OptiTime

تضم هذه الوثيقة ثمانية مخططات نشاط لأهم حالات الاستخدام في النظام، تتبع الجدول الدراسي من إدخال أوقات التفرّغ إلى بنائه ونشره، ثم تسجيل المقررات وجدولة الامتحانات ونشر العلامات، ومعها المساعد الذكي. ويُظهر كل مخطط سير عمل المستخدم وحده: الخطوات التي يقوم بها والأسئلة التي تحدد خطوته التالية، دون ما يجري داخل النظام.

**الملفات:** كود كل مخطط في مجلد `Src` وصورته في مجلد `Images` بالاسم نفسه، والكود في هذه الوثيقة مطابق حرفياً لملفات `Src`.

## قواعد الرسم

- يُظهر المخطط ما يفعله المستخدم وما يقرره فقط، ولا يُظهر ما يجري داخل النظام.
- كل معيّن سؤال، وعلى كل فرع منه جوابه «نعم» أو «لا».
- كل فرع ينتهي بخطوة أو بنهاية أو يعود إلى خطوة سابقة، فلا فروع فارغة ولا معيّنات بلا سؤال.
- يُذكر الفاعل تحت العنوان، وحين يشارك في سير العمل أكثر من شخص يكون لكل منهم عمود.

| الرمز | معناه |
|---|---|
| دائرة سوداء | بداية سير العمل |
| دائرة بنقطة داخلها | نهاية سير العمل |
| مستطيل بزوايا مستديرة | خطوة يقوم بها المستخدم |
| معيّن أصفر | سؤال يحدد الخطوة التالية |
| سهم يعود إلى خطوة سابقة | تكرار الخطوات حتى يتغير الجواب |

## فهرس المخططات

| الرقم | الحالة | الفاعل |
|---|---|---|
| 1 | UC-27 إدخال أوقات التفرّغ | عضو هيئة التدريس |
| 2 | UC-29 توليد الجدول الدراسي | منسق الجداول والموارد |
| 3 | UC-61 معالجة تعارضات الجدول ومؤشر الجودة | منسق الجداول والموارد |
| 4 | UC-31 اعتماد الجدول ونشره | موظف الشؤون الأكاديمية، ومنسق الجداول والموارد |
| 5 | UC-67 تسجيل المقررات | الطالب |
| 6 | UC-84 جدولة الامتحانات | موظف شؤون الامتحانات |
| 7 | UC-80 الإدخال المزدوج واعتماد الكشوف ونشرها | موظف شؤون الامتحانات |
| 8 | UC-105 محادثة المساعد الذكي | أي مستخدم في النظام |

---

## UC-27: إدخال أوقات التفرّغ

**الفاعل:** عضو هيئة التدريس. **سير العمل:** يختار المدرّس الفصل، فإن كانت نافذة التفرّغ مغلقة اطّلع على أسبوعه دون تعديل. وإن كانت مفتوحة حدد أوقاته على شبكة الأسبوع وسبب كل وقت مغلق، ثم يسلّم الأسبوع إلى المنسق إن اكتمل، أو يحفظه مسودة ليكمله لاحقاً.

![UC-27: إدخال أوقات التفرّغ](Images/UC-27.png)

<div dir="ltr">

```plantuml
@startuml UC-27
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-27 — إدخال أوقات التفرّغ\n<size:13><color:#455A64>الفاعل: عضو هيئة التدريس</color></size>

start
:يفتح صفحة أوقات التفرّغ;
:يختار الفصل الدراسي;
if (هل نافذة إدخال التفرّغ مفتوحة؟) then (لا)
  :يطّلع على أسبوعه
  للقراءة فقط;
  stop
else (نعم)
  :يحدد على شبكة الأسبوع
  أوقاته المفضّلة والمتاحة والمغلقة;
  :يختار سبب كل وقت مغلق
  ويكتب ملاحظة للمنسق إن رغب;
  if (هل اكتمل أسبوعه؟) then (نعم)
    :يسلّم الأسبوع
    إلى المنسق;
    stop
  else (لا)
    :يحفظ الأسبوع مسودة
    ليكمله لاحقاً;
    stop
  endif
endif
@enduml
```

</div>

---

## UC-29: توليد الجدول الدراسي

**الفاعل:** منسق الجداول والموارد. **سير العمل:** يختار المنسق نطاق التوليد والخوارزمية ويبدأ التوليد. فإن فشل اطّلع على السبب وراجع الشعب والقاعات وأوقات التفرّغ ثم أعاد المحاولة. وإن نجح راجع الجدول المولَّد وعدّل مواضع محاضراته عند الحاجة، ثم يضيفه إلى نسخة الجدول أو يلغي المعاينة.

![UC-29: توليد الجدول الدراسي](Images/UC-29.png)

<div dir="ltr">

```plantuml
@startuml UC-29
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-29 — توليد الجدول الدراسي\n<size:13><color:#455A64>الفاعل: منسق الجداول والموارد</color></size>

start
:يفتح الجدول الأسبوعي
على النسخة المطلوبة;
repeat :يختار نطاق التوليد\nكل الكليات أو كلية أو قسم;
  :يختار خوارزمية التوليد
  الجينية أو التراجع والتتبع;
  :يبدأ التوليد
  وينتظر انتهاءه;
  backward :يطّلع على سبب الفشل
  ويراجع الشعب والقاعات
  وأوقات التفرّغ;
repeat while (هل فشل التوليد؟) is (نعم) not (لا)
:يراجع الجدول المولَّد
ومقاييس جودته;
:يعدّل مواضع المحاضرات
بالسحب والإفلات عند الحاجة;
if (هل يقبل الجدول المولَّد؟) then (نعم)
  :يضيفه إلى نسخة الجدول;
  stop
else (لا)
  :يلغي المعاينة
  فتبقى المسودة كما هي;
  stop
endif
@enduml
```

</div>

---

## UC-61: معالجة تعارضات الجدول ومؤشر الجودة

**الفاعل:** منسق الجداول والموارد. **سير العمل:** إن خلت النسخة من التعارضات اطّلع المنسق على مؤشر الجودة وانتهى. وإلا عالج التعارضات واحداً بعد آخر بحل مقترح أو بنقل المحاضرة يدوياً، حتى لا يبقى تعارض صلب ويبلغ مؤشر الجودة حدّه الأدنى.

![UC-61: معالجة تعارضات الجدول ومؤشر الجودة](Images/UC-61.png)

<div dir="ltr">

```plantuml
@startuml UC-61
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-61 — معالجة تعارضات الجدول ومؤشر الجودة\n<size:13><color:#455A64>الفاعل: منسق الجداول والموارد</color></size>

start
:يفتح لوحة التعارضات
لنسخة الجدول;
if (هل في النسخة تعارضات؟) then (لا)
  :يطّلع على مؤشر الجودة
  وخلو النسخة من التعارضات;
  stop
else (نعم)
  repeat :يختار تعارضاً من القائمة;
    :يطّلع على الحلول المقترحة
    وأثر كل حل على مؤشر الجودة;
    :يطبّق الحل المناسب بنقرة
    أو ينقل المحاضرة يدوياً;
  repeat while (هل بقيت تعارضات صلبة\nأو المؤشر دون حدّه الأدنى؟) is (نعم) not (لا)
  stop
endif
@enduml
```

</div>

---

## UC-31: اعتماد الجدول ونشره

**الفاعلان:** موظف الشؤون الأكاديمية، ومنسق الجداول والموارد. **سير العمل:** يراجع موظف الشؤون الأكاديمية النسخة المرسلة للاعتماد. فإن كانت لديه ملاحظات أرجعها إلى المنسق فيعالجها ويعيد إرسالها، ويتكرر ذلك حتى لا تبقى ملاحظات، ثم يعتمد الموظف النسخة وينشر الجدول للمدرّسين والطلاب.

![UC-31: اعتماد الجدول ونشره](Images/UC-31.png)

<div dir="ltr">

```plantuml
@startuml UC-31
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-31 — اعتماد الجدول ونشره

|#F1F8FE|موظف الشؤون الأكاديمية|
|#F3FAF3|منسق الجداول والموارد|
|موظف الشؤون الأكاديمية|
start
:يفتح نسخة الجدول
المرسلة للاعتماد;
:يراجع محاضراتها وقائمة التحقق
ويقارنها بالنسخة السارية;
while (هل لديه ملاحظات على النسخة؟) is (نعم)
  :يكتب ملاحظاته على المحاضرات
  ويُرجع النسخة إلى المنسق;
  |منسق الجداول والموارد|
  :يعالج الملاحظات
  ويعيد إرسال النسخة;
  |موظف الشؤون الأكاديمية|
  :يراجع النسخة من جديد;
endwhile (لا)
:يعتمد النسخة;
:ينشر الجدول
للمدرّسين والطلاب;
stop
@enduml
```

</div>

---

## UC-67: تسجيل المقررات

**الفاعل:** الطالب. **سير العمل:** إن منع فحص الأهلية الطالب من التسجيل اطّلع على السبب وانتهى. وإلا أضاف مقرراته إلى السلة واحداً بعد آخر وهو يعاين جدوله الأسبوعي، ثم يؤكد التسجيل ويعالج أي مشكلة تظهر في السلة، حتى يحصل على رقم التأكيد وجدوله وفاتورته.

![UC-67: تسجيل المقررات](Images/UC-67.png)

<div dir="ltr">

```plantuml
@startuml UC-67
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-67 — تسجيل المقررات\n<size:13><color:#455A64>الفاعل: الطالب</color></size>

start
:يفتح صفحة التسجيل
ويطّلع على فحص الأهلية;
if (هل يُسمح له بالتسجيل الآن؟) then (لا)
  :يطّلع على سبب المنع
  كإغلاق النافذة أو عائق مالي
  أو نقص تصريح المرشد;
  stop
else (نعم)
  repeat :يبحث في المقررات المطروحة\nويختار مقرراً وشعبه;
    :يضيفه إلى السلة
    ويعاين جدوله الأسبوعي;
  repeat while (هل يريد إضافة مقرر آخر؟) is (نعم) not (لا)
  :يضغط تأكيد التسجيل;
  while (هل ظهرت مشكلات في السلة\nكتعارض أو شعبة ممتلئة؟) is (نعم)
    :يستبدل الشعبة أو يحذف المقرر
    أو ينضم إلى قائمة الانتظار;
    :يضغط تأكيد التسجيل من جديد;
  endwhile (لا)
  :يطّلع على رقم التأكيد
  وجدوله الأسبوعي وفاتورته;
  stop
endif
@enduml
```

</div>

---

## UC-84: جدولة الامتحانات

**الفاعل:** موظف شؤون الامتحانات. **سير العمل:** يعرّف الموظف فترة الامتحانات وفتراتها اليومية وقواعدها ويولّد قائمة الامتحانات، ثم يولّد الجدول ويعيد توليده بعد زيادة الفترات أو تعديل القواعد حتى لا يبقى امتحانان متعارضان لطلاب مشتركين. وبعد مراجعة الجدول يكمل شروط النشر الناقصة ثم ينشره.

![UC-84: جدولة الامتحانات](Images/UC-84.png)

<div dir="ltr">

```plantuml
@startuml UC-84
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-84 — جدولة الامتحانات\n<size:13><color:#455A64>الفاعل: موظف شؤون الامتحانات</color></size>

start
:ينشئ فترة امتحانات
بنوعها وتاريخيها;
:يحدد الفترات اليومية
وقواعد الامتحانات;
:يولّد قائمة الامتحانات
ويدمج شعب المقرر أو يفصلها;
repeat :يولّد جدول الامتحانات;
  :يطّلع على نتيجة التوزيع;
  backward :يزيد الفترات
  أو يعدّل القواعد;
repeat while (هل بقيت امتحانات متعارضة\nلطلاب مشتركين؟) is (نعم) not (لا)
:يراجع الجدول وينقل امتحاناً
يدوياً عند الحاجة;
while (هل بقيت شروط نشر\nغير متحققة؟) is (نعم)
  :يكمل الشرط الناقص
  كتوزيع المقاعد والمراقبين;
endwhile (لا)
:ينشر جدول الامتحانات
للطلاب والمدرّسين;
stop
@enduml
```

</div>

---

## UC-80: الإدخال المزدوج واعتماد الكشوف ونشرها

**الفاعل:** موظف شؤون الامتحانات. **سير العمل:** يُدخل الموظف علامة الامتحان النهائي في كل كشف راجعه القسم، ويحسم كل فرق بين إدخاله وإدخال المدرّس بملاحظة، ثم يعتمد الكشف. وبعد اعتماد الكشوف كلها يختار كشوف قسم أو كلية وينشرها بعد تأكيد هويته.

![UC-80: الإدخال المزدوج واعتماد الكشوف ونشرها](Images/UC-80.png)

<div dir="ltr">

```plantuml
@startuml UC-80
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-80 — الإدخال المزدوج واعتماد الكشوف ونشرها\n<size:13><color:#455A64>الفاعل: موظف شؤون الامتحانات</color></size>

start
repeat :يفتح كشفاً راجعه القسم;
  :يُدخل علامة الامتحان النهائي لكل طالب
  أو يستورد ملف التحقق;
  :يطّلع على الفروقات
  بين إدخاله وإدخال المدرّس;
  while (هل بقي فرق غير محلول؟) is (نعم)
    :يختار العلامة الصحيحة
    ويكتب ملاحظة;
  endwhile (لا)
  :يعتمد الكشف;
repeat while (هل بقيت كشوف لم تُعتمد؟) is (نعم) not (لا)
:يختار الكشوف المعتمدة
لقسم أو كلية;
:يضغط نشر
ويؤكد هويته;
stop
@enduml
```

</div>

---

## UC-105: محادثة المساعد الذكي

**الفاعل:** أي مستخدم في النظام. **سير العمل:** إن لم يكن المساعد متاحاً للمستخدم أكمل عمله من الشاشات المعتادة. وإلا سأل ما يشاء وقرأ كل إجابة ومصدرها، ثم ينفّذ الإجراء المقترح في شاشته المختصة إن وُجد، أو يغلق المساعد.

![UC-105: محادثة المساعد الذكي](Images/UC-105.png)

<div dir="ltr">

```plantuml
@startuml UC-105
skinparam dpi 150
' ===== النمط الموحّد =====
skinparam defaultFontName Tahoma
skinparam shadowing false
skinparam roundcorner 10
skinparam defaultTextAlignment center
skinparam ArrowColor #37474F
skinparam ActivityBackgroundColor #FFFFFF
skinparam ActivityBorderColor #546E7A
skinparam ActivityDiamondBackgroundColor #FFF8E1
skinparam ActivityDiamondBorderColor #FFB300
skinparam ActivityStartColor #37474F
skinparam ActivityEndColor #37474F
skinparam SwimlaneBorderColor #90A4AE
skinparam SwimlaneTitleFontSize 14
skinparam SwimlaneTitleFontStyle bold
' ===== المخطط =====
title UC-105 — محادثة المساعد الذكي\n<size:13><color:#455A64>الفاعل: أي مستخدم في النظام</color></size>

start
:يفتح نافذة المساعد
من أي شاشة;
if (هل المساعد متاح له الآن؟) then (لا)
  :يكمل عمله
  من الشاشات المعتادة;
  stop
else (نعم)
  repeat :يكتب سؤاله\nأو يختار سؤالاً مقترحاً;
    :يقرأ الإجابة ومصدرها
    ويقيّمها إن رغب;
  repeat while (هل لديه سؤال آخر؟) is (نعم) not (لا)
  if (هل اقترحت الإجابة إجراءً؟) then (نعم)
    :يضغط بطاقة الإجراء
    ويُتمه في الشاشة المختصة;
    stop
  else (لا)
    :يغلق نافذة المساعد;
    stop
  endif
endif
@enduml
```

</div>

---

</div>
