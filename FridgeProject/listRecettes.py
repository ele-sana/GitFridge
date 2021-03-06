from django.db.models.manager import RelatedManager

from FridgeApp.models import Aliments


pateCarbonara = Recettes(name="Pâtes carbonara")
pateCarbonara.save()
chiconGratin = Recettes(name ="Chicon aux gratin")
chiconGratin.save()
gratinDePateAuJambon = Recettes(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes(name ="Omelette campagnarde")
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes(name ="Soupe de haricots verts")
soupeDeHaricotVert.save()
tartiflette = Recettes(name ="Tartiflette")
tartiflette.save()
gratindeCourgette = Recettes(name ="Gratin de Courgettes")
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes(name ="Boulets à la Liégeoise")
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes(name ="Cabillaud en papillotes")
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes(name ="Carbonades à la Flamande")
carbonadeFlamande.save()
pouletAigreDoux = Recettes(name ="Ooulet aigre-doux")
pouletAigreDoux.save()
tomatesFarcies = Recettes(name ="Tomates farcies")
tomatesFarcies.save()
hachisParmentier = Recettes(name ="Hachis Parmentier")
hachisParmentier.save()



# les photos

chiconGratin= Recettes.objects.get(name ="Chicon aux gratin")
chiconGratin.picture="https://www.delhaize.lu/fr/file/17185.recipes-single/ab1b17658717113d6691351550c56847/358aef34bc1b421c88e18babebe182c0.jpg"
chiconGratin.save()
gratinDePateAuJambon = Recettes.objects.get(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.picture("https://fac.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Ffac.2F2018.2F07.2F30.2F1ab55c0f-e57d-45ca-96ee-d8028fe5f161.2Ejpeg/850x478/quality/90/crop-from/center/gratin-de-pates-au-jambon.jpeg")
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes.objects.get(name ="Omelette campagnarde")
omeletteCampagnarde.picture("http://p9.storage.canalblog.com/93/96/163138/8595921.jpg")
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes.objects.get(name ="Soupe de haricots verts")
soupeDeHaricotVert.picture("https://www.recette360.com/wp-content/uploads/2019/04/Soupe-de-haricots-verts-et-pommes-de-terre-au-thermomix-696x468.jpg")
soupeDeHaricotVert.save()
tartiflette = Recettes.objects.get(name ="Tartiflette")
tartiflette.picture("https://assets.afcdn.com/recipe/20160401/38946_w1024h768c1cx2690cy1793.jpg")
tartiflette.save()
gratindeCourgette = Recettes.objects.get(name ="Gratin de Courgettes")
gratindeCourgette.picture("https://assets.afcdn.com/recipe/20190529/93185_w1024h1024c1cx2736cy1824.jpg")
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes.objects.get(name ="Boulets à la Liégeoise")
bouletsALaLiegeoise.picture("https://gourmandiz.dhnet.be/app/uploads/2018/03/bouletsliegeois.jpg")
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes.objects.get(name ="Cabillaud en papillotes")
cabillaudEnPapillote.picture("https://cac.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Fcac.2F2018.2F09.2F25.2F344c426d-a028-4e0d-8b0c-013a027622f1.2Ejpeg/750x562/quality/80/crop-from/center/cr/wqkgUm91dnJhaXMvIFByaXNtYXBpeCAvIEN1aXNpbmUgQWN0dWVsbGU%3D/filet-de-cabillaud-en-papillote.jpeg")
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes.objects.get(name ="Carbonades à la Flamande")
carbonadeFlamande.picture("https://cac.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Fcac.2F2018.2F09.2F25.2Fbda9f46a-20a2-4bd0-a854-bbd4cca95294.2Ejpeg/750x562/quality/80/crop-from/center/cr/wqkgRnJhbmNpcyBLT01QQUxJVENIL1BSSVNNQVBJWCAvIEN1aXNpbmUgQWN0dWVsbGU%3D/carbonade-flamande.jpeg")
carbonadeFlamande.save()
pouletAigreDoux = Recettes.objects.get(name ="Ooulet aigre-doux")
pouletAigreDoux.picture("https://res.cloudinary.com/hv9ssmzrz/image/fetch/c_fill,f_auto,h_600,q_auto,w_800/https://s3-eu-west-1.amazonaws.com/images-ca-1-0-1-eu/recipe_photos/original/178622/pinterest.png")
pouletAigreDoux.save()
tomatesFarcies = Recettes.objects.get(name ="Tomates farcies")
tomatesFarcies.picture("https://www.papillesetpupilles.fr/wp-content/uploads/2014/08/Tomates-Farcies-HD.jpg")
tomatesFarcies.save()
hachisParmentier = Recettes.objects.get(name ="Hachis Parmentier")
hachisParmentier.picture("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgWFRUYGBgaGhwYGhocGh4YGhoYHBgZGhoYGhghIS4lHB4rIRoaJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHhISHjQrIysxNDQ9Nj00NjQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQxNDQ0NDQ0NDQ0NDQ0NDQ0NP/AABEIALwBDAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwEEBQAGB//EAD4QAAEDAgQEAwYDBgYCAwAAAAEAAhEDIQQSMUEFUWFxgZHwIjKhscHhE0LRBhRSYnLxFSOCkrLSB5MzQ+L/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/xAArEQACAgEDAgUEAwEBAAAAAAAAAQIRAxIhMUFRBBMiMmFCgZGhcbHRwVL/2gAMAwEAAhEDEQA/APo5YhLVZyKMi5HE1srFigtVksQ5UqHYmF2VNLFOVGkLEwiCOF0I0jsBTKKEJSoDsyLMhXBKgCJU5kK5KgDDkYckqQUgG51welZ1GdAFjMozpIcpDkAOD1OZIzLsyAHZ134iQXrg5IdDvxFP4iryuzoCh/4ij8RIzqC5Ayz+IoNRVi9dmSsVDy9LdUSy5Lc9A6GOeuFRVy9TnQFGsQoRlq7KuyjCxRCiE7KoISoLE5UJanFq7KlQWJhT4phagLUNDsAhCfVk6FGVLSOxUKC1OyqMqWkdiFwCfCHKp0jsWFxeiLEGVDQ7JKhcVxU0BE9lGbsuK6EqA7MozKCV2ZKgJL1xegLkMpFDM6jOglQUUAeZcXpR7KCUANL0JelkoS5Awy9CX9UsuQOegBjnKPxOqS5yHMgD1mVcpXQu45jiEJCKEMJAQ4KMqMrg1FDALVxamFqEhFBYvKuIRkoCpoYBQuRPeBrHikPxbBq4LKWWC5aGoyfCGZlE9FWdxJuwJ8EDuJHZh8So86PRN/YvQ+pcHYqHDoVQPEH7Mb5of36pyZ5fZJ5W/pYaflF0lRmVP98qc2/7V373U5t/2pa32f5Cl3LeZQSqwxT98njb7rjjT/Cw9iR8wFm/ExTprf8AktY5NWh5QkpX72PzMcOxCNuIpnct7iPiq8yPW0TpZxKgpoa0+65p8UD6cahUnF8MGmuRZCglSQohVQWCShJUlCXJUMjMhL0UIHOSoCSUt7kDnICUDJc5R62QEogkB7NcFBK6V3HMSuUSplAHAKUMpNfFNZqZPIa+PJTKcYq5OkNJt0hxck1cQ1upWZWxz3e7YfDz3Vf8Odb/AC8lzPNKXsVLuzTRFe5lypxIfkbPVVn4l7t47KIXQoeO/c2/6DVXCoWWTqSfH9FzaYGgTFBeqUYx4Qm2+TsqkMXUwXe6J67eaY9obcy7tp5rOeeEFuyowlJ0heRSafOye2pcw0QIki+uw5lVa7ZHsuLSD7U7jkBdc0/GP6V+TWOG36mG9zGiZmOsKs7HyPZgHoIAHMu9FJLGWc4kuuA2xgk2MffwU1cIBLnFp5gW7DwsuSWWc+WdUcUI9DqlcezA1JmCBJtJ9oCfFcavMSDsLzFtrAKtjqophsNDyLwJytLt+p6rLxFV3vPa9jCQ0Eu21Ot9FCj2NoxtGxiHOdDg/KAbgfI85U0sc0yHezEXNge3orO4jUYC1jHOY0FpzNPvXvJ3HTdUeI4icjxdxlpdoSASBYCw78uy2xznHZP/AATwxmt1/p6g0xrbuP1RNc8aPPjf7ry+DryT/nPbobQG6zAtfXdb3DuIMqCGukgXI0PkuuOeE9sir56HJk8PKG8XZfbiv42T1b+n90bcrvccOxsUvKgdTBXQsbq4P/qObVvUkNewjUJRCNlRzbe8OR1TGBrvdMHkUvMadTVfPQqr4KxCU9ys1Gxqk5VrRImChcE1zEtFDsWQuCMqEqCz15KhDK4FdVmAxchCzuJ4r8jbbvPIfw9Cfl3WeXKscW2VGLk6R2L4hctYehd15N/X0KjWT73l+vNdTYB9OiIuXLFOb1ZOei6I0k1H0x/Pc5QSoJQPfGq0ciKGFyUaknKJJOwuVZ/BDWBzhmc4S1sxroO6zMRxCo1rw1rQ8TABGUcieey5cvidL0xV/wBG+PC5bmg3CuvmIEbAyfE6D4pDjSm8GIn2nHU6wDB7LMw76xb/AJ1WMt3GzWkbg2gj6ao2V6JGam4Pc0fxa/zRvqei5JTlLdv8cHTHAo7cmpW4mxrsuYydABttNonoE/8AeMwABgHQxuddliYJ1QAGpYG7f4nAgxB/KNBOt1L6tRlvw2i86gmOUkmNgsbdl+VHhF52LLszQXADU5Yi+oVXEY4MIbGbQzvM6kRHl5qlW4yzO5hDjFpDgJi0meqs1MU1wH4bdY0HtE7pFqFcoXTc/MXNIgmcsARrojw7ySQ4wTDZNzrcNaNTYb2VfEV8n5bujUjMBtPIoMRVLfze0AI2kHv4aIWxo42BxbEua5wYZym8weUx49VS4xSdVa1znyWgWGjSecWFo9BPp4XMRLXjNJLrERPIomYXIbOFjZxby0Jtf7KlKuClSruZuF4c5rC9zosbFskxsBsNUnFvNwwOymAXOZ7Mg3AnReggWbAe4nUx31+yRVkNgMGbeIi/z+yfmbjTbPOupj3ZJs2YNgTe3xHmvR8IwLKDJY4TEHKD+bWSgHD3uEObB5gR4kLRwXD2tAALz1JF/CESy2qRM5KgsNiw0e/4R81pYau1+mqqP4cDrp8Vo4TDtYIatPCyyQkq4fQ4s7xyi+5xYhdT8+atFiEsXtuKapnAmID5s/wKF9OCnupoW8j4Fc0ovF6o8dV2/g0jJS2fJTLUstVt7LpbmLZVJWg42KhZ3UZVYdTQZEUFnoQjY1LBTmrZGRFaoGNc47DzOw87eKwrzcyT7TjzJ9fJa/Eh7IHNw+En5wsc7nr/AGXDm9eZRfCV/dm0PTC+rCLlwKFoTGhaEEFVa7TEnwH1VxtPMY21P6IatzOw0+pXJmm3LQvubY0luwsTXLSDvAkf6YMeZVOgWucAA6TIIAtF/pAWfxLjtMVA3MJMidRMxfkehRUa8w4b3BG4XPoa3N1cUMxHDGOa5pcbugjN7M8rCdviqWHwlNmYtblA0zDQT70GxFt+i0KNe0ADUGd5S+J5XZ2bHLqbQBcADsPErN8Ubwm26bHMxTfZGcOJEAhgMTG/6c1n8fxNGmSC4y0XcHbwLZRpMq5RotYz2CGAAAmLyYIgnT7LOxvD2Euc4uc9xuWjXnt2SWlWpFRrVZXY1lbLlm18hIMxy5yZKsYfDvbAaRJktEkR0nYhLwPDIh2U2te3wVmtXLGgBjpBJdaB0IA7DXrokzRyt0iXMaWNLg7NzEETeb6x35KrjWBzs2a5O8X305ahVxXzEmXHW0C09JXUa2X2SAb2nSyVUUo0XqTS4yR2g2ja06K01vgNTEx8UrCOz/kg8wI23O6v08C6ReB2uo9TfpRlKcVyUn0yeU84v8Eilgn/AIgi/O5XoqGHDevdG5oBmFtDDJ7yMZeIraIjD4UC58tlcY0DZKFQc1V4rxVlFuZxuZgbmNV0RxJcHO5Sk6L9QgXJWYeMMFUUg4EuhoIMwXGJPjC8Vxv9qar6MBuXMS2dZIBLW62mJ7NKxuD1D+I2oCZa8HKTa5OWPFs9lssW1jUK9x9pyOb7LteexXEIafFqVZh9oNcIkEgXJiRzEoGVge+/dd0JK9N3/hxSi+Qy1C5kog9FK1pMkq1tJ5a9vV0okHkrNQa9QsthI8CR5GFx4vRklj6co6HvFSLLmocg5Lm1OaPMOnkumjKzUYfXoKw02VammBypCZGO91v9XzCzMllpYgy0gdx3F/lKqNv43XG1Wdp9Uv0areC+GVcqJqY9iXC2omyxhjAeenyBVPEUw5hadCCNY21nZOHuPbzbbwWW/FDIXGIDTM9BeVxuHrZtHhM+YY8tNXOGlwLHEmSQ4glsgjcGL9FpcJ40aTMtUQcxytF4b0jZYGKxjiS1sNawuytFoY++Xw5n6JdYFzwXSS4Z4AgwRMkDSZ05LfRapm2pcM+rUXBzZaZ0QPaV4fguNewNe2o1rYaXsIiwIEiCbRvEgnRetw/FGPAIsSJjlM37WXJPFQU47rgutcYI9mTpIkC2sbnunZCzKWnNDczibAaSZ3N/iVXAkSFO0EZhyWDiaRyEs4g2fa7zeTvsirS/3SCOX16qnTwmYmbAAwBEDwWrgaGVvcXWOhye3BrKcY7rkTh8ECDLWyeQgo28IBIOkbfVaFOAVbZButoYe5zyzy6Fajhg37+rJ8RdYX7QftLTwwggudybt/UdtlgYj9t89L2GGTALp8TA7Arojj7IzqUt2e2r4lrRJIC8lx/9qIAZR9oueGFwI9mftN143HcbfiH5S/2AbEWDQdSfW6qNxhLoaxsO2BMyQASepy/VbRxdxXGCtms7jNVjw4PMDMbkZXESNtbafdU8fjXPdL35nCQSYIg5tekRI6JJY0VAxwb7N4OxgAtA0MwOY8UNQlheBHvyDaSCQY7TAO60jBLg1crObVcQ4ZvZa5oHJ0MIHsjrPmE/C1gzUCIy26AAn7bSfCth6Ty0tY2ztTEAT/D6subwt+jn25Ba6G0ZPIkz1oY2q9hB1c0jvt22XtsUC17o6f8AEL5rhKha6m0al7QPNfS8Q7M5x5n7BYKLWS/gmXtIZiSNVbp4mVQLVwsuhSaMXFM1XPny/RZlITJ/mPzKa15DC7d3stHPYfH5LqdPLA5CO/VYYfX4iUlwlRcvTjS7glimDzCdCiDy9ea7aMbLrHpgeqzKnJMDzyUpgx4f6+qqTldl0B06Hdv1HTsU19Ux94VTE0y4SPeHXXkJ2OsHbtIWWfE5JSjyi8bSdPhlstlLcxV8Djw45HWeLEG0/ofWi0cspYsiyLs+qCUXF/BTAheF49iHMrupusx1xyI+q+hPprB4/wANbVEOFxdrhq07EFOUN0yoyrY+bcS4MWFtWnTztElw943BFgfy6WHJYjcRmJgEOgiQDqdo0jUQvoVAPonJUFtA/wDKf+p6eSp8X/Z5tSalKGP7SHdxz6qqsak0eOpvcGctHCDrBALcvP2h5FMxLXMdnc4jchpIJP5rzAdBv1CX+65KmTEf5YBzTHISYPIkAX6dU2rS/EL3tqAtBazMfZl8e17NzA59R2UOO5tGfY9RwHjrcga9xLpgE7nYDmtfB8TbUktILb/ovn+GfTY6SXPc0OiPZboIi07Ov2UsxctN3NAGjHQZkxM6xIk9AsJYU3sVs9+p9QoVxEyrFLH09C9oNxEiV88bxcuoBsy8giBuRsR1WU+pmeG5zmc6TLj7tyOun0WccLBpPk+k8Q4/SYC7MHQYjmY0nl12uvK4Hj+IY97nVCQ4E2gwTBhg2gFZ2IDajA7KYkNv7JIcTGoIkzHaFQ/ei5rWRlcJfJFssG0A+ydO11rHHSGlGIWNxjnuzl92kHf2nPib+APghxmIa5ntNiSRaLlzSWOB2MBKpsDWzBALp/1R8NZQMoOOkvktLWQTAEkAnoCFskTKWzDGHaGQCdwSd73BUUaZmYvyifh4KzRrgtYHQGggPMXB0MhbP7yxlHPTykzkDi1wLCQTmi887JU3ycU9LbplTD8IqOdmdAncxPgNzfVa2H4GxpkiTzPPtovJsr+3mfNSCfeJIO/lN4XseFcZFUFrsrXjQD8wi5A281cZRW1D81t0OfQA2WViXiVcxuL2CVhuFuqGXyGct3d+Q6IlKzRKjv2XwJq121D7jPd6kansvoZasrhdEMgAQAIWy1kqUgk7ElqJlHMem56J4YBcmBuUBcHCTIp7bOqduTP5t9lnOTb0Q3f9DSVXLgj3iHD3RZg5nQv7DQdZ5I2mRdC5+a57QLADYAbCAiauvDhWKNL7mM5uTslrVCMBd5rRoSAa7v68FOYqq1/qU1jlgmW0Me7t5qAQOS4lSAb39aK0SypjsG2o2ZyuGjm6i+ltRPoKvhuLvokMxAzN0FRt5/qHr6rRItr9VWxIEGRO1ws8mGMnqWz7lRyNbPdG1QxLHtDmuDgdwZCp4mCV51jchlhcx38vun+phsfgmN40QYqtj+YSWnw1CyeScNsi27otQjL2v7GlUwzXCCAQdlQdwot/+N0D+F12+B1b8R0V2hjGPuHDvqPPbxVtlORIII6XW0Jwlw7IlGUeTyfF+DsqtiqyP5tQOocNPGF4Pi3AKlF2ZvtU9ZEmLDUbzGvVfaxTKr1+GMfOZgvrFp7xqr0iU6PhVKsGwQQTJG/K/hfdNZVbkk++DkkH3mw7bmIHmvpnEf8Ax7QqElj30ybmIIPcW+a8/iP/ABjXaD+HiGOnZwcz5ZlDxs1jmR41xyj2mk5YAINjOhNrGBorTMO972vAkGD0kA+z2MCAtZ/7CY1sZqbHhotkeInmZg/BPwv7PVmB+dpaXHQTAAkjL0lJxaNFOLMb96eaTjpleCBEWhoJ7WAHJXqGAL2HK0km9yADOgJF7DlzWrh+Bge8HOvOhjt2WtTw8CACBygpKHcl5OxgD9nQ5gDn5dCQOcQbnb7KzS4Y6mBkvHmtoM6H13Uhh2b5lXsuDNtvk8xxWk5zHBzYLi3LDYOefennEDwVtuAy03MNL3jmJB/PES0E2GtupW5kcdwPih/dh+Yl3c/QKWZ6VZ47C8NLQ5jmkuBBYWwSBfM0jcaa/rN/D/s64vD2l1MB0i8mLezEaa+a9NTpAe60DsrVGgTskOMEUMNw5jbxJ5m5+y0WM5BPZhhqT+nnon03iJYMw0kQGz/WYaT0ElZPLFOrt9lubKLe4zBUYN1dfigDlYC52sDUDm46NHUpDKBPvGBybLR4uPtHwDe6fkDGw0ADWBYTz6nqZPVVHHlyfC/ZEpQj8v8AQlokzUIcdQwXpt/q/jPw7qazy4kkz3Vd7jK4OI0XXjwxxrZGMpSk7Y+nsnAlV2P+XLzVgH4K2xJB5l2dCXfogLlJSK4TGqAxSAudGjGSpDvUfZJlEHXVpk0MVXE7jtt65qw1/b1olPvdVYqMXEv+P6/dVqz/AF4K/iaB9QsrE2b65FOworF0GRY8xYqxheKOaffjqQfi5t/gsyvVgqs56ylgxy3a3+NjRZZLaz22H4u/ZzH9nNcfBsh/wT/8fymHsIPKcp/2uA+a+fPcuOJeLZjHKbeWilYZx9sn99x64v3JfY+ls45SOpc3u0n/AIymt4vQP/2sHc5fnC+UGodiR/S5zfkQp/e6m1R4/wBrv+TSVS85dn+iaxPuj68zFMdo9h7OB+ql7GO5FfIRjKn8YP8AUxp+UI2Yurt+H/6z/wB07y9l+Q04/wD0z6jV4cw6WVGrw2NHBeCZja5gTS/9Z/7rv8Qrj81PwZ/+1L81/T+xpQXX9HrKtPLqW+YSmmdL9r/JebGNxBt+MW/0taPmCm021H+9Xqu8Wt/4tCWjM+iQ9WNdWb+Q727w35wk1sZRZ79VjehdJ8gs2nwhh9/O/wDqe93wJV8cLpsYclNjbTZonrdUvD5XzJL+EJ5Ma4TYDeOM0psqVD/KzKP9xsjHEMQ/3WMpjm453fGQPJRhqd4039FWXOhNeEi/c2xee/pSRYwGFc8zUe55Hb4Azl/0wvQ0WsFwLxqbujaXG581kYJ+vdXPxvXgNlvDFCHtSRjKcpcsuPduqlapslOr7T68kLnyBMTz9bK2xJEB6Y312KQ7168k0O7KHIpRGM5o2vSZQuf6+KVlUWXVOqAv7KuaiHN1+JUtjouypDkgORh/VYpl0MhSG9fiELXo5VITAdbf4rhp5780yFAEfDZMRVrCR9/ssfG0DFp0K9AGBIq4YGTHIbdEAjxGJw5lVn0yF63EcOHJZtfA3RqaKqzzjksrcdw9A7hqakS4mH+qlbB4Yo/w5WpC0mU0JtNmivjBQVYoYP4JponSZ9OkbetZupdQuJW9SwQ5D7z+qQ/DgO9etVdioz6FCfmtPC0bx08tCipUdYt94TWsM+fkRba17osWktMpgR9t0dcDL5x8D9ks6+uSl0lqepBpKP4kEdPD69UeeZ5+roMqY1sKHMpRL2FFrch07q0SquFdA9eCaagv/ZLUPSS/Vc1yWXiNvsoBHLy7lJyHpGud0P2RfidN0hz/AF4WQuepbHRZzoHOlI/E+f0XZkrHQx5KGHJZeV2b1ZIZoAKQ5cULt1mMa1yIP9WSR681wTTCi01yIkT/AGSdkZVioYFEDp8Fzfr9Ufr4oJEvYCNvgqmIoBaE+vFA5A0zDqUNYSS1bVRguqNamLpNFJlEssgdPJNb9V3LxSsKK0dEzD7W1TXsHxUUdB63KdhQ+i4T681Vru9rfUq0zXz/AOSr12CfP6ocmJIYw29ev7IRUvvp05FDT0Ph8lxCephSHtq305jzRkg7G6rjVEPr9E7ChTx6gajwUnsfL7KHdyiU2OhtGw39eCIu7/NC0evJM3TsKAdU6+tl34ia5gj1zVXdKwoP8RcXevFLRFFgcX6rgfXwQuTG6oAOm3p8FYp2Hr9ELE0FCEz/2Q==")
hachisParmentier.save()

# les recettes
pateCarbonara = Recettes.objects.get(name'=Pâtes carbonara")
pateCarbonara.howToCook('https://www.marmiton.org/recettes/recette_pates-a-la-carbonara_80453.aspx')
pateCarbonara.save()
chiconGratin= Recettes.objects.get(name ="Chicon aux gratin")
chiconGratin.howToCook("https://www.marmiton.org/recettes/recette_endives-chicons-au-gratin-belgique_27819.aspx")
chiconGratin.save()
gratinDePateAuJambon = Recettes.objects.get(name ="Gratin de pâtes au jambon")
gratinDePateAuJambon.howToCook("https://www.marmiton.org/recettes/recette_gratin-de-pates-au-jambon_334460.aspx")
gratinDePateAuJambon.save()
omeletteCampagnarde = Recettes.objects.get(name ="Omelette forestière")
omeletteCampagnarde.howToCook("https://www.marmiton.org/recettes/recette_omelette-campagnarde_82950.aspx")
omeletteCampagnarde.save()
soupeDeHaricotVert = Recettes.objects.get(name ="Soupe de haricots verts")
soupeDeHaricotVert.howToCook("https://www.marmiton.org/recettes/recette_veloute-d-haricots-verts_41016.aspx")
soupeDeHaricotVert.save()
tartiflette = Recettes.objects.get(name ="Tartiflette")
tartiflette.howToCook("https://www.marmiton.org/recettes/recette_tartiflette-facile_15733.aspx")
tartiflette.save()
gratindeCourgette = Recettes.objects.get(name ="Gratin de Courgettes")
gratindeCourgette.howToCook("https://www.marmiton.org/recettes/recette_gratin-de-courgettes-rapide_17071.aspx")
gratindeCourgette.save()
bouletsALaLiegeoise= Recettes.objects.get(name ="Boulette à la Liégeoise")
bouletsALaLiegeoise.howToCook("https://www.marmiton.org/recettes/recette_boulets-a-la-liegeoise_32638.aspx")
bouletsALaLiegeoise.save()
cabillaudEnPapillote = Recettes.objects.get(name ="Cabillaud en papillotes")
cabillaudEnPapillote.howToCook("https://www.marmiton.org/recettes/recette_filet-de-cabillaud-en-papillote_19058.aspx")
cabillaudEnPapillote.save()
carbonadeFlamande = Recettes.objects.get(name ="Carbonades à la Flamande")
carbonadeFlamande.howToCook("https://www.marmiton.org/recettes/recette_carbonades-flamandes-traditionnelles_29711.aspx")
carbonadeFlamande.save()
pouletAigreDoux = Recettes.objects.get(name ="Ooulet aigre-doux")
pouletAigreDoux.howToCook("https://www.marmiton.org/recettes/recette_poulet-aigre-doux_23788.aspx")
pouletAigreDoux.save()
tomatesFarcies = Recettes.objects.get(name ="Tomates farcies")
tomatesFarcies.howToCook("https://www.marmiton.org/recettes/recette_tomates-farcies-facile_63622.aspx")
tomatesFarcies.save()
hachisParmentier = Recettes.objects.get(name ="Hachis Parmentier")
hachisParmentier.howToCook("https://www.marmiton.org/recettes/recette_hachis-parmentier_17639.aspx")
hachisParmentier.save()




google = Recettes(name="Google")
google.save()
google = Recettes.objects.get(name ="Google")
google.howToCook("https://www.google.be/")
google.save()




# creations des  recettes








.objects.get
# /lien avec les recettes
ratatouille=Recettes(name= "ratatouille provençale")
ratatouille.save()
ratatouille=Recettes.objects.get(name= "ratatouille provençale")
ratatouille.picture="https://assets.afcdn.com/recipe/20180412/78543_w768h583c1cx2779cy1994cxb5558cyb3988.webpp"
ratatouille.howToCook="https://www.marmiton.org/recettes/recette_ratatouille-provencale_80582.aspx"
ratatouille.save()
ratatouille.aliments.add
ratatouille.save()


chouDeBruxellesAuLardons=Recettes(name="Choux de Bruxelles aux lardons")
chouDeBruxellesAuLardons.save()
chouDeBruxellesAuLardons=Recettes.objects.get(name="Choux de Bruxelles aux lardons")
chouDeBruxellesAuLardons.picture="https://assets.afcdn.com/recipe/20181017/82830_w1200h1600c1cx1752cy2336cxb3504cyb4672.webp"
chouDeBruxellesAuLardons.howToCook="https://www.marmiton.org/recettes/recette_choux-de-bruxelles-au-lard-en-cocotte_28770.aspx"
chouDeBruxellesAuLardons.save()

desDeNavetsBeurre=Recettes(name="Dés de navets au beurre")
desDeNavetsBeurre.save()
desDeNavetsBeurre=Recettes.objects.get(name="Dés de navets au beurre")
desDeNavetsBeurre.howToCook=("https://assets.afcdn.com/recipe/20181017/82830_w1200h1600c1cx1752cy2336cxb3504cyb4672.webp")
desDeNavetsBeurre.picture="https://assets.afcdn.com/recipe/20210112/117145_w768h583c1cx1060cy707cxb2121cyb1414.webp"
desDeNavetsBeurre.save()

gratinDeChouFleur=Recettes(name="Gratin de Choux-fleur")
gratinDeChouFleur.save()
gratinDeChouFleur=Recettes.objects.get(id=29)
gratinDeChouFleur.picture="https://assets.afcdn.com/recipe/20170112/49501_w1200h1800c1cx2000cy3000.webp"
gratinDeChouFleur.howToCook="https://assets.afcdn.com/recipe/20210112/117145_w768h583c1cx1060cy707cxb2121cyb1414.webp"
gratinDeChouFleur.save()

epinarCreme=Recettes(name="Epinards crémeux")
epinarCreme.save()
epinarCreme=Recettes.objects.get(name="Epinards crémeux")
epinarCreme.picture="https://assets.afcdn.com/recipe/20200430/110237_w1200h800c1cx2726cy1817cxb5453cyb3635.webp"
epinarCreme.howToCook="https://www.marmiton.org/recettes/recette_epinards-cremeux_27147.aspx"
epinarCreme.save()

pouletOrange=Recettes(name="Poulet à l'orange")
pouletOrange.save()
pouletOrange=Recettes.objects.get(name="Poulet à l'orange")
pouletOrange.picture="https://assets.afcdn.com/recipe/20210304/118355_w768h583c1cx1060cy707cxb2121cyb1414.webp"
pouletOrange.howToCook="https://www.marmiton.org/recettes/recette_poulet-a-l-orange_12721.aspx"
pouletOrange.save()

FricasseePoulet=Recettes(name="Fricassée de poulet au paprika et poivrons")
FricasseePoulet.save()
FricasseePoulet=Recettes.objects.get(name="Fricassée de poulet au paprika et poivrons")
FricasseePoulet.picture="https://assets.afcdn.com/recipe/20100120/44027_w768h583c1cx192cy256.webp"
FricasseePoulet.howToCook="https://www.marmiton.org/recettes/recette_fricasse-de-poulet-au-paprika-et-poivrons_22552.aspx"
FricasseePoulet.save()


ratatouille=Recettes.objects.get(name= "ratatouille provençale")
FricasseePoulet=Recettes.objects.get(name="Fricassée de poulet au paprika et poivrons")
chouDeBruxellesAuLardons=Recettes.objects.get(name="Choux de Bruxelles aux lardons")
pouletOrange=Recettes.objects.get(name="Poulet à l'orange")
epinarCreme=Recettes.objects.get(name="Epinards crémeux")
desDeNavetsBeurre=Recettes.objects.get(name="Dés de navets au beurre")
gratinDeChouFleur=Recettes.objects.get(id=29)
