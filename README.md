# Manhattan, Oklid ve Chebyshev Uzaklığı Hesaplama

`variables` değeri içerisinde yer boyutlar yer almaktadır.

```
variable = [
    [0, 1, 2, 3, 4],
    [1, 0, 1, 2, 3],
    [2, 1, 0, 1, 2],
    [3, 2, 1, 0, 1],
    [4, 3, 2, 1, 0]
]
```

Örnek olarak yukarıda bilgiler verilmiştir. Bu değerleri dilediğiniz gibi değiştirerek farklı sonuçlar elde edebilirsiniz.

## Nasıl Kullanabilirim?

Manhattan uzaklığını hesaplamak için;
```
calcManhattan(variable)
```

Oklid uzaklığını hesaplamak için;
```
calcTaxicab(variable)
```

Chebyshev uzaklığını hesaplamak için;
```
calcChebyshev(variable)
```

## Örnek Sonuçlar
### Manhattan Uzaklığı Hesaplaması

```
----- Manhattan Uzaklığı Hesaplaması -----
|0-0|+|1-1|+|2-2|+|3-3|+|4-4| = (0+0+0+0+0) = 0
|0-1|+|1-0|+|2-1|+|3-2|+|4-3| = (1+1+1+1+1) = 5
|0-2|+|1-1|+|2-0|+|3-1|+|4-2| = (2+0+2+2+2) = 8
|0-3|+|1-2|+|2-1|+|3-0|+|4-1| = (3+1+1+3+3) = 11
|0-4|+|1-3|+|2-2|+|3-1|+|4-0| = (4+2+0+2+4) = 12
|1-0|+|0-1|+|1-2|+|2-3|+|3-4| = (1+1+1+1+1) = 5
|1-1|+|0-0|+|1-1|+|2-2|+|3-3| = (0+0+0+0+0) = 0
|1-2|+|0-1|+|1-0|+|2-1|+|3-2| = (1+1+1+1+1) = 5
|1-3|+|0-2|+|1-1|+|2-0|+|3-1| = (2+2+0+2+2) = 8
|1-4|+|0-3|+|1-2|+|2-1|+|3-0| = (3+3+1+1+3) = 11
|2-0|+|1-1|+|0-2|+|1-3|+|2-4| = (2+0+2+2+2) = 8
|2-1|+|1-0|+|0-1|+|1-2|+|2-3| = (1+1+1+1+1) = 5
|2-2|+|1-1|+|0-0|+|1-1|+|2-2| = (0+0+0+0+0) = 0
|2-3|+|1-2|+|0-1|+|1-0|+|2-1| = (1+1+1+1+1) = 5
|2-4|+|1-3|+|0-2|+|1-1|+|2-0| = (2+2+2+0+2) = 8
|3-0|+|2-1|+|1-2|+|0-3|+|1-4| = (3+1+1+3+3) = 11
|3-1|+|2-0|+|1-1|+|0-2|+|1-3| = (2+2+0+2+2) = 8
|3-2|+|2-1|+|1-0|+|0-1|+|1-2| = (1+1+1+1+1) = 5
|3-3|+|2-2|+|1-1|+|0-0|+|1-1| = (0+0+0+0+0) = 0
|3-4|+|2-3|+|1-2|+|0-1|+|1-0| = (1+1+1+1+1) = 5
|4-0|+|3-1|+|2-2|+|1-3|+|0-4| = (4+2+0+2+4) = 12
|4-1|+|3-0|+|2-1|+|1-2|+|0-3| = (3+3+1+1+3) = 11
|4-2|+|3-1|+|2-0|+|1-1|+|0-2| = (2+2+2+0+2) = 8
|4-3|+|3-2|+|2-1|+|1-0|+|0-1| = (1+1+1+1+1) = 5
|4-4|+|3-3|+|2-2|+|1-1|+|0-0| = (0+0+0+0+0) = 0
```

### Oklid Uzaklığı Hesaplaması

```
----- Oklid Uzaklığı Hesaplaması -----
|0-0|²+|1-1|²+|2-2|²+|3-3|²+|4-4|²=√(0.0+0.0+0.0+0.0+0.0) = 0
|0-1|²+|1-0|²+|2-1|²+|3-2|²+|4-3|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|0-2|²+|1-1|²+|2-0|²+|3-1|²+|4-2|²=√(2.0+0.0+2.0+2.0+2.0) = 16
|0-3|²+|1-2|²+|2-1|²+|3-0|²+|4-1|²=√(3.0+1.0+1.0+3.0+3.0) = 29
|0-4|²+|1-3|²+|2-2|²+|3-1|²+|4-0|²=√(4.0+2.0+0.0+2.0+4.0) = 40
|1-0|²+|0-1|²+|1-2|²+|2-3|²+|3-4|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|1-1|²+|0-0|²+|1-1|²+|2-2|²+|3-3|²=√(0.0+0.0+0.0+0.0+0.0) = 0
|1-2|²+|0-1|²+|1-0|²+|2-1|²+|3-2|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|1-3|²+|0-2|²+|1-1|²+|2-0|²+|3-1|²=√(2.0+2.0+0.0+2.0+2.0) = 16
|1-4|²+|0-3|²+|1-2|²+|2-1|²+|3-0|²=√(3.0+3.0+1.0+1.0+3.0) = 29
|2-0|²+|1-1|²+|0-2|²+|1-3|²+|2-4|²=√(2.0+0.0+2.0+2.0+2.0) = 16
|2-1|²+|1-0|²+|0-1|²+|1-2|²+|2-3|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|2-2|²+|1-1|²+|0-0|²+|1-1|²+|2-2|²=√(0.0+0.0+0.0+0.0+0.0) = 0
|2-3|²+|1-2|²+|0-1|²+|1-0|²+|2-1|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|2-4|²+|1-3|²+|0-2|²+|1-1|²+|2-0|²=√(2.0+2.0+2.0+0.0+2.0) = 16
|3-0|²+|2-1|²+|1-2|²+|0-3|²+|1-4|²=√(3.0+1.0+1.0+3.0+3.0) = 29
|3-1|²+|2-0|²+|1-1|²+|0-2|²+|1-3|²=√(2.0+2.0+0.0+2.0+2.0) = 16
|3-2|²+|2-1|²+|1-0|²+|0-1|²+|1-2|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|3-3|²+|2-2|²+|1-1|²+|0-0|²+|1-1|²=√(0.0+0.0+0.0+0.0+0.0) = 0
|3-4|²+|2-3|²+|1-2|²+|0-1|²+|1-0|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|4-0|²+|3-1|²+|2-2|²+|1-3|²+|0-4|²=√(4.0+2.0+0.0+2.0+4.0) = 40
|4-1|²+|3-0|²+|2-1|²+|1-2|²+|0-3|²=√(3.0+3.0+1.0+1.0+3.0) = 29
|4-2|²+|3-1|²+|2-0|²+|1-1|²+|0-2|²=√(2.0+2.0+2.0+0.0+2.0) = 16
|4-3|²+|3-2|²+|2-1|²+|1-0|²+|0-1|²=√(1.0+1.0+1.0+1.0+1.0) = 5
|4-4|²+|3-3|²+|2-2|²+|1-1|²+|0-0|²=√(0.0+0.0+0.0+0.0+0.0) = 0
```

### Chebyshev Uzaklığı Hesaplaması

```
----- Chebyshev Uzaklığı Hesaplaması -----
|0-0|,|1-1|,|2-2|,|3-3|,|4-4| = (<0>,<0>,<0>,<0>,<0>)
|0-1|,|1-0|,|2-1|,|3-2|,|4-3| = (<1>,<1>,<1>,<1>,<1>)
|0-2|,|1-1|,|2-0|,|3-1|,|4-2| = (<2>, 0 ,<2>,<2>,<2>)
|0-3|,|1-2|,|2-1|,|3-0|,|4-1| = (<3>, 1 , 1 ,<3>,<3>)
|0-4|,|1-3|,|2-2|,|3-1|,|4-0| = (<4>, 2 , 0 , 2 ,<4>)
|1-0|,|0-1|,|1-2|,|2-3|,|3-4| = (<1>,<1>,<1>,<1>,<1>)
|1-1|,|0-0|,|1-1|,|2-2|,|3-3| = (<0>,<0>,<0>,<0>,<0>)
|1-2|,|0-1|,|1-0|,|2-1|,|3-2| = (<1>,<1>,<1>,<1>,<1>)
|1-3|,|0-2|,|1-1|,|2-0|,|3-1| = (<2>,<2>, 0 ,<2>,<2>)
|1-4|,|0-3|,|1-2|,|2-1|,|3-0| = (<3>,<3>, 1 , 1 ,<3>)
|2-0|,|1-1|,|0-2|,|1-3|,|2-4| = (<2>, 0 ,<2>,<2>,<2>)
|2-1|,|1-0|,|0-1|,|1-2|,|2-3| = (<1>,<1>,<1>,<1>,<1>)
|2-2|,|1-1|,|0-0|,|1-1|,|2-2| = (<0>,<0>,<0>,<0>,<0>)
|2-3|,|1-2|,|0-1|,|1-0|,|2-1| = (<1>,<1>,<1>,<1>,<1>)
|2-4|,|1-3|,|0-2|,|1-1|,|2-0| = (<2>,<2>,<2>, 0 ,<2>)
|3-0|,|2-1|,|1-2|,|0-3|,|1-4| = (<3>, 1 , 1 ,<3>,<3>)
|3-1|,|2-0|,|1-1|,|0-2|,|1-3| = (<2>,<2>, 0 ,<2>,<2>)
|3-2|,|2-1|,|1-0|,|0-1|,|1-2| = (<1>,<1>,<1>,<1>,<1>)
|3-3|,|2-2|,|1-1|,|0-0|,|1-1| = (<0>,<0>,<0>,<0>,<0>)
|3-4|,|2-3|,|1-2|,|0-1|,|1-0| = (<1>,<1>,<1>,<1>,<1>)
|4-0|,|3-1|,|2-2|,|1-3|,|0-4| = (<4>, 2 , 0 , 2 ,<4>)
|4-1|,|3-0|,|2-1|,|1-2|,|0-3| = (<3>,<3>, 1 , 1 ,<3>)
|4-2|,|3-1|,|2-0|,|1-1|,|0-2| = (<2>,<2>,<2>, 0 ,<2>)
|4-3|,|3-2|,|2-1|,|1-0|,|0-1| = (<1>,<1>,<1>,<1>,<1>)
|4-4|,|3-3|,|2-2|,|1-1|,|0-0| = (<0>,<0>,<0>,<0>,<0>)
```

`<rakam>` en büyük ifadeyi temsil etmektedir.