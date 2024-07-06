import polars as pl
import datashader as ds
from datashader import transfer_functions as tf
import plotly.io as pio
import numpy as np


def func():
    # CSV 파일 읽기, 필요한 컬럼 선택
    dong_list = ["송도동", "청라동", "중산동"]
    file_path = '.'

    file_name = "utf_인천광역시_온도_202107.csv" # 파일 이름은 여기 수정하면됨

    df = pl.read_csv(f'{file_path}/{file_name}')

    dff = df.select(['위도', '경도', '온도']).to_pandas()


    # Datashader Canvas 설정
    cvs = ds.Canvas(plot_width=3200, plot_height=4800)

    # 포인트를 그리고, '온도' 컬럼을 사용하여 색상 지정
    agg = cvs.points(dff, x='경도', y='위도', agg=ds.mean('온도'))

    v = agg.values

    vmin = np.nanmin(v)
    vmax = np.nanmax(v)

    # print("최저 평균 온도 : ", vmin)
    # print("최고 평균 온도 : ", vmax)

    # agg is an xarray object, see http://xarray.pydata.org/en/stable/ for more details
    coords_lat, coords_lon = agg.coords['위도'].values, agg.coords['경도'].values

    # Corners of the image, which need to be passed to mapbox
    coordinates = [[coords_lon[0], coords_lat[0]],
                [coords_lon[-1], coords_lat[0]],
                [coords_lon[-1], coords_lat[-1]],
                [coords_lon[0], coords_lat[-1]]]
    # print(coordinates)

    df # 데이터 출력


    from colorcet import fire
    import datashader.transfer_functions as tf
    import matplotlib.cm as cm

    # 점 크기 변경
    agg = tf.spread(agg, px=3)
    # img = tf.shade(agg, cmap=['blue', 'green', 'red'], how='linear')[::-1].to_pil()
    img = tf.shade(agg, cmap=cm.coolwarm, alpha=180)[::-1].to_pil()

    # Pillow를 사용하여 블러 필터 적용
    from PIL import ImageFilter
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=1))
    # blurred_img.show()



    import plotly.express as px
    # Trick to create rapidly a figure with mapbox axes
    fig = px.scatter_mapbox(dff[:1], lat='위도', lon='경도', zoom=12, opacity=1, height=1200) # height 바꾸면 맵 이미지 바뀜 이거 바꿔야함
    # Add the datashader image as a mapbox layer image
    fig.update_layout(mapbox_style="carto-positron",
                    mapbox_layers = [
                    {
                        "sourcetype": "image",
                        "source": blurred_img,
                        "coordinates": coordinates
                    }]
    )


    fig.show()
