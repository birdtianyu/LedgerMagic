# author:Hongkun Xu 
# datetime:2020/03/02 14:34
# software: PyCharm
"""
説明：用于计算
"""
import numpy as np


def DetectPoints(dst):
    """
    计算四个基准点坐标

    Args:
        dst: 图像矩阵

    Returns: 四个基准点坐标

    """
    # 图片一半的宽度
    HalfWidth = (dst.shape[1] + 1) // 2

    # 线的坐标
    NoneZeroRows = np.where(dst > 0)[0]
    NoneZeroCols = np.where(dst > 0)[1]

    # 查找的行范围
    row = sorted(list(set(NoneZeroRows)))

    MaxNumber = 0
    RowFirstHead = 0
    RowSecondHead = 0
    RowBottom = 0

    # 搜索间隔最大的两条线
    for i in range(len(row)):
        if i + 1 < len(row):
            if row[i + 1] - row[i] > MaxNumber:
                # RowFirstHead = RowSecondHead
                RowFirstHead = i
                MaxNumber = row[i + 1] - row[i]
                RowSecondHead = i
                RowBottom = i + 1
            # 　誤差設定
            elif row[i + 1] - row[i] > 4:
                RowSecondHead = i

    # 裁剪起始行
    StartLine = row[RowFirstHead]
    # 裁剪结束行
    FinishLine = row[RowBottom]

    # 计算上面的线宽
    lineWidth = 0
    TopParts = [NoneZeroRows[i] for i in range(len(NoneZeroCols)) if NoneZeroCols[i] == HalfWidth and NoneZeroRows[i] <= StartLine]
    TopParts.sort()
    for i in range(len(TopParts)-1, 1, -1):
        # 误差设置
        if TopParts[i] - TopParts[i-1] != 1:
            lineWidth = TopParts[len(TopParts)-1] - TopParts[i]
            break

    print("上部线宽: ", lineWidth)

    # 最上面的第一行不一定就是上端端点
    # 最下面的第一行不一定就是下端端点
    StartLine = StartLine - int(0.2*lineWidth)
    FinishLine = FinishLine + int(0.2*lineWidth)

    print("起始行: ", StartLine)
    print("结束行: ", FinishLine)

    StartCols = [NoneZeroCols[i] for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == StartLine]
    FinishCols = [NoneZeroCols[i] for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == FinishLine]

    print("开始判断上线方向")
    print("判断基准: ", min(StartCols), HalfWidth, max(StartCols))

    LeftTop = []
    RightTop = []

    minCol = min(StartCols)
    maxCol = max(StartCols)

    # 上端
    if minCol > HalfWidth:
        # 上面右端点
        print("上部左上方向")
        RightTop = [max(StartCols), StartLine]
    elif maxCol < HalfWidth:
        # 上面左端点
        print("上部右上方向")
        LeftTop = [min(StartCols), StartLine]
    else:
        # 进一步验证
        print("进一步验证")
        UpLine = [NoneZeroCols[i] for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == StartLine-int(0.2*lineWidth)]
        if min(UpLine) < minCol:
            # 上面右端点
            print("上部左上方向")
            RightTop = [max(StartCols), StartLine]
        elif max(UpLine) > maxCol:
            # 上面左端点
            print("上部右上方向")
            LeftTop = [min(StartCols), StartLine]
        else:
            # 上部水平线
            print("上部水平线")
            LeftTop = [min(StartCols), StartLine]
            RightTop = [max(StartCols), StartLine]

    LeftBottom = []
    RightBottom = []

    minCol = min(FinishCols)
    maxCol = max(FinishCols)
    
    # 下端
    if minCol > HalfWidth:
        # 下面右端点
        print("下部左下方向")
        RightBottom = [max(FinishCols), FinishLine]
    elif maxCol < HalfWidth:
        # 下面左端点
        print("下部右下方向")
        LeftBottom = [min(FinishCols), FinishLine]
    else:
        # 进一步验证
        print("进一步验证")
        downLine = [NoneZeroCols[i] for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == FinishLine + int(0.2 * lineWidth)]
        if min(downLine) < minCol:
            # 下面右端点
            print("下部左下方向")
            RightBottom = [max(FinishCols), FinishLine]
        elif max(downLine) > maxCol:
            # 下面左端点
            print("下部右下方向")
            LeftBottom = [min(FinishCols), FinishLine]
        else:
            # 下部水平线
            print("下部水平方向")
            LeftBottom = [min(FinishCols), FinishLine]
            RightBottom = [max(FinishCols), FinishLine]


    # 2.计算下下界
    step = 2
    FinFinishLine = FinishLine + step
    while FinFinishLine in NoneZeroRows:
        FinFinishLine = FinFinishLine + step

    # 3.计算另一个下部端点
    BottomArea = [i for i in range(len(NoneZeroRows)) if FinishLine < NoneZeroRows[i] < FinFinishLine]
    Rows = [NoneZeroRows[i] for i in BottomArea]
    Cols = [NoneZeroCols[i] for i in BottomArea]

    if len(LeftBottom) == 0:
        # 左下方向
        MinCols = min(Cols)
        index = Cols.index(MinCols)
        LeftBottom = [MinCols, Rows[index]]

    elif len(RightBottom) == 0:
        # 右下方向
        MaxCols = max(Cols)
        index = Cols.index(MaxCols)
        RightBottom = [MaxCols, Rows[index]]

    print("下端两点:", LeftBottom, RightBottom)

    # 下端两端点高度差
    Height_difference = FinFinishLine - FinishLine

    Top = True
    SmallRow = StartLine
    SmallCol = HalfWidth
    BigRow = StartLine
    BigCol = HalfWidth
    MaxCount = 10
    Count = MaxCount
    if len(LeftTop) == 0:
        # 左半部分
        # 向上2像素步长搜索
        print("最后计算左上角坐标")
        for last in range(StartLine-1, 0, -2):
            TopArea = [i for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == last and NoneZeroCols[i] <= HalfWidth]
            if len(TopArea) > 0:
                Top = False
                TopAreaRow = [NoneZeroRows[i] for i in TopArea]
                TopAreaCol = [NoneZeroCols[i] for i in TopArea]
                if min(TopAreaCol) < SmallCol and Count != 0:
                    # クリア
                    Count = MaxCount
                    SmallCol = min(TopAreaCol)
                    SmallRowIndex = TopAreaCol.index(SmallCol)
                    SmallRow = TopAreaRow[SmallRowIndex]
                elif Count == 0:
                    break
                else:
                    Count = Count - 1
            elif not Top:
                break
            else:
                pass

        LeftTop = [SmallCol, SmallRow]

    elif len(RightTop) == 0:
        # 右半部分
        # 向上2像素步长搜索
        print("最后计算右上角坐标")
        for last in range(StartLine - 1, 0, -2):
            TopArea = [i for i in range(len(NoneZeroRows)) if NoneZeroRows[i] == last and NoneZeroCols[i] >= HalfWidth]
            if len(TopArea) > 0:
                Top = False
                TopAreaRow = [NoneZeroRows[i] for i in TopArea]
                TopAreaCol = [NoneZeroCols[i] for i in TopArea]
                if max(TopAreaCol) > BigCol and Count != 0:
                    # クリア
                    Count = MaxCount
                    BigCol = max(TopAreaCol)
                    BigRowIndex = TopAreaCol.index(BigCol)
                    BigRow = TopAreaRow[BigRowIndex]
                elif Count == 0:
                    break
                else:
                    Count = Count - 1
            elif not Top:
                break
            else:
                pass

        RightTop = [BigCol, BigRow]

    print("上面两端点:", LeftTop, RightTop)

    # 补足
    # 头部提升
    LeftTop[1] = LeftTop[1] - int(0.4*lineWidth)
    RightTop[1] = RightTop[1] - int(0.4*lineWidth)
    # 尾部下沉
    LeftBottom[1] = LeftBottom[1] + int(0.4*lineWidth)
    RightBottom[1] = RightBottom[1] + int(0.4*lineWidth)

    return LeftTop, RightTop, LeftBottom, RightBottom









