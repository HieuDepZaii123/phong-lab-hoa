# Vá index.html đã có patch3 — một lần.
# Thêm Điều chế các chất và Ứng dụng thực tế trong Kiến thức cơ bản.
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
s = p.read_text(encoding="utf-8")

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:70], s.count(old))
    s = s.replace(old, new)

rep(
"return e===`rx`||e===`tools`||e===`see`||e===`eq`||e===`grade`?e:`safe`",
"return e===`rx`||e===`prep`||e===`use`||e===`tools`||e===`see`||e===`eq`||e===`grade`?e:`safe`"
)
rep(
"],[`rx`,`Các loại phản ứng`]],primers=",
"],[`rx`,`Các loại phản ứng`],[`prep`,`Điều chế các chất`],[`use`,`Ứng dụng thực tế`]],primers="
)
rep(
"Nền ngắn trước khi vào bài: chọn bài lớp 10, làm từng bước, xem hiện tượng, rồi trả lời câu hỏi. Phần kết luận đầy đủ vẫn nằm trong từng thí nghiệm.",
"Nền ngắn trước khi vào bài: chọn bài lớp 10, làm từng bước, xem hiện tượng, rồi trả lời câu hỏi. Mục Điều chế và Ứng dụng nói chất trong các bài được làm ra và dùng ở đâu. Kết luận đầy đủ vẫn nằm trong từng thí nghiệm."
)

cards = r"""
,prep=[{name:`Hidro H2`,how:`Trong lab: kim loại đứng trước H (Zn, Fe) tác dụng axit không oxi hóa. Không dùng HNO3 hay H2SO4 đặc nóng — không thu được H2.`,eq:[`Zn + 2HCl → ZnCl2 + H2↑`],ind:`Hơi nước qua metan, xúc tác Ni, nhiệt cao: CH4 + H2O ⇌ CO + 3H2. Cũng điện phân nước.`,labs:`Điều chế và thử tính chất khí hidro.`},{name:`Muối tan (thí dụ NaCl)`,how:`Axit tác dụng bazơ: HCl + NaOH → NaCl + H2O. Đây là cách lab minh họa, không phải cách lấy muối ăn.`,eq:[`HCl + NaOH → NaCl + H2O`],ind:`Muối ăn lấy từ nước biển (cô đặc) hoặc mỏ muối. NaOH và Cl2 công nghiệp lại được điện phân từ chính NaCl.`,labs:`Phản ứng trung hòa có phenolphtalein.`},{name:`Xà phòng`,how:`Đun chất béo với NaOH, rồi thêm NaCl bão hòa để xà phòng nổi. KOH cho xà phòng mềm.`,eq:[`(C17H33COO)3C3H5 + 3NaOH → 3C17H33COONa + C3H5(OH)3`],ind:`Cùng phản ứng: dầu mỡ động thực vật + NaOH (rắn) hoặc KOH (lỏng).`,labs:`Xà phòng hóa chất béo.`},{name:`Etyl axetat`,how:`Đun cách thủy axit axetic với ancol etylic, xúc tác H2SO4 đặc. Phản ứng thuận nghịch, hiệu suất không hoàn toàn.`,eq:[`CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O`],ind:`Cùng kiểu este hóa, có khi dùng xúc tác khác và tách nước liên tục để đẩy cân bằng.`,labs:`Điều chế etyl axetat.`},{name:`Đồng từ dung dịch CuSO4`,how:`Điện phân dung dịch CuSO4 với điện cực trơ: Cu bám catot (−), O2 thoát ở anot (+), dung dịch thành H2SO4.`,eq:[`2CuSO4 + 2H2O → 2Cu + O2↑ + 2H2SO4`],ind:`Tinh luyện đồng: anot là đồng thô, catot là lá đồng mỏng, dung dịch CuSO4. Đồng tinh khiết bám catot.`,labs:`Điện phân dung dịch CuSO4.`},{name:`Muối Fe2+ và Fe3+`,how:`Fe + HCl hoặc H2SO4 loãng cho muối Fe2+. Muối Fe3+ điều chế bằng chất oxi hóa mạnh hơn, thí dụ clo. Fe2+ cũng sinh ra khi Fe đẩy Cu2+.`,eq:[`Fe + 2HCl → FeCl2 + H2↑`,`2Fe + 3Cl2 → 2FeCl3`],ind:`Muối sắt thương mại thường từ sắt vụn với axit, hoặc từ quặng sau khi hòa tách.`,labs:`Nhận biết Fe2+ và Fe3+. KMnO4 oxi hóa Fe2+ trong axit (Fe2+ thành Fe3+, mất màu tím).`},{name:`Nhôm hidroxit`,how:`Nhỏ NH3 vào dung dịch muối Al3+. Không dùng NaOH dư vì Al(OH)3 tan thành Na[Al(OH)4].`,eq:[`AlCl3 + 3NH3 + 3H2O → Al(OH)3↓ + 3NH4Cl`],ind:`Kết tủa từ muối nhôm bằng bazơ yếu, hoặc trung hòa aluminat.`,labs:`Tính lưỡng tính của nhôm.`},{name:`Glucozơ`,how:`Bài trong app không điều chế glucozơ; chỉ chứng minh nhóm –CHO và nhiều –OH. Trong lab THPT, glucozơ lấy từ thủy phân tinh bột hoặc saccarozơ (H+, đun).`,eq:[`(C6H10O5)n + nH2O → nC6H12O6`,`C12H22O11 + H2O → C6H12O6 (glucozơ) + C6H12O6 (fructozơ)`],ind:`Thủy phân tinh bột (ngô, sắn) bằng enzim hoặc axit loãng.`,labs:`Tráng bạc của glucozơ. Glucozơ với Cu(OH)2. Saccarozơ không tráng bạc nếu chưa thủy phân.`},{name:`Lớp bạc trên gương`,how:`Đun cách thủy anđehit hoặc glucozơ với thuốc thử Tollens mới pha. Bạc kim loại bám thành lớp rất mỏng — không phải luyện bạc từ quặng.`,eq:[`C6H12O6 + 2[Ag(NH3)2]OH → C6H12O7 + 2Ag↓ + 4NH3 + H2O`],ind:`Gương công nghiệp cũng khử muối bạc trên mặt kính sạch, rồi phủ sơn bảo vệ.`,labs:`Phản ứng tráng gương. Tráng bạc của glucozơ.`},{name:`Polietilen và PVC`,how:`Bài trong app không trùng hợp; chỉ đun để phân biệt. PE điều chế bằng trùng hợp etilen. PVC bằng trùng hợp vinyl clorua.`,eq:[`nCH2=CH2 → (–CH2–CH2–)n`,`nCH2=CHCl → (–CH2–CHCl–)n`],ind:`Trùng hợp trong bình phản ứng có xúc tác, áp suất (PE) hoặc huyền phù (PVC).`,labs:`PE và PVC khi đun nóng.`},{name:`Làm mềm nước cứng`,how:`Nước cứng tạm thời: đun sôi, Ca(HCO3)2 thành CaCO3. Cả tạm thời và vĩnh cửu: Na2CO3 kết tủa Ca2+ (và Mg2+).`,eq:[`Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O`,`CaCl2 + Na2CO3 → CaCO3↓ + 2NaCl`],ind:`Nhà máy còn dùng nhựa trao đổi ion hoặc thẩm thấu ngược khi cần nước rất mềm.`,labs:`Làm mềm nước cứng tạm thời.`}
],use=[{name:`Hidro`,uses:[`Tổng hợp amoniac, rồi ra phân đạm.`,`Hidro hóa dầu thực vật lỏng (làm bơ thực vật, shortening).`,`Nhiên liệu tên lửa và pin nhiên liệu.`,`Hàn cắt kim loại khi đốt với oxi.`],labs:`Điều chế và thử tính chất khí hidro.`},{name:`Muối ăn và muối trung hòa`,uses:[`Gia vị và ướp thực phẩm.`,`Điện phân dung dịch NaCl có màng ngăn: NaOH, Cl2, H2.`,`Điện phân NaCl nóng chảy: natri kim loại và clo.`,`Nước muối sinh lí trong y tế.`],labs:`Phản ứng trung hòa có phenolphtalein.`},{name:`Xà phòng`,uses:[`Giặt quần áo và rửa tay.`,`Tẩy dầu mỡ vì phần dài của anion “thích” dầu, đầu –COO- “thích” nước.`,`Chất nhũ hóa trong một số mỹ phẩm.`],labs:`Xà phòng hóa chất béo.`},{name:`Etyl axetat`,uses:[`Dung môi sơn, mực in và keo.`,`Hương trái cây trong thực phẩm (liều rất nhỏ).`,`Tẩy sơn móng tay.`],labs:`Điều chế etyl axetat.`},{name:`Đồng`,uses:[`Dây dẫn điện và mạch in vì dẫn điện tốt.`,`Hợp kim: đồng thau (với kẽm), đồng thanh (với thiếc).`,`Ống dẫn nước, mái nhà, đồng xu.`,`Muối CuSO4: thuốc trừ nấm trong nông nghiệp, và bể điện phân.`],labs:`Điện phân dung dịch CuSO4. Pin Daniell Zn–Cu dùng Cu2+ làm chất oxi hóa.`},{name:`Muối sắt(II) và sắt(III)`,uses:[`FeSO4: bổ sung sắt, xử lý nước, mực.`,`FeCl3: keo tụ cặn trong nước thải.`,`Thép và gang là ứng dụng lớn của sắt kim loại, không phải của hai muối này.`],labs:`Nhận biết Fe2+ và Fe3+. KMnO4 oxi hóa Fe2+ trong axit.`},{name:`Nhôm hidroxit`,uses:[`Thuốc kháng axit dạ dày (liều dược phẩm).`,`Chất độn chống cháy trong nhựa.`,`Keo tụ làm trong nước.`],labs:`Tính lưỡng tính của nhôm.`},{name:`Glucozơ`,uses:[`Nguồn năng lượng của tế bào.`,`Truyền tĩnh mạch khi người bệnh không ăn được.`,`Lên men thành etanol.`,`Tráng gương và một số đường kẹo.`],labs:`Tráng bạc của glucozơ. Glucozơ với Cu(OH)2.`},{name:`Gương bạc`,uses:[`Gương soi và gương trang trí.`,`Bình thủy: lớp bạc giữ nhiệt.`,`Một số linh kiện quang học.`],labs:`Phản ứng tráng gương. Tráng bạc của glucozơ.`},{name:`Polietilen (PE)`,uses:[`Túi, màng bọc thực phẩm, chai.`,`Ống dẫn nước lạnh và vỏ cáp.`,`Đun nhẹ thì mềm, nguội rắn lại — hàn nhiệt các mối nối ống PE.`],labs:`PE và PVC khi đun nóng.`},{name:`PVC`,uses:[`Ống nước, khung cửa, vỏ dây điện.`,`Da giả và một số áo mưa.`,`Không đốt rác PVC: sinh HCl, ăn mòn và độc.`],labs:`PE và PVC khi đun nóng.`},{name:`Nước đã làm mềm`,uses:[`Nồi hơi: ít cặn CaCO3, đỡ tốn nhiên liệu và đỡ nổ ống.`,`Giặt: xà phòng không bị Ca2+, Mg2+ kết tủa thành cặn.`,`Pha chế trong phòng lab khi cần tránh ion Ca2+, Mg2+.`],labs:`Làm mềm nước cứng tạm thời.`}]
""".replace("\n","")
rep(
"Làm nơi thoáng.`}];return",
"Làm nơi thoáng.`}]" + cards + ";return"
)

prep_view = r"""
(0,I.jsxs)(`div`,{className:`flex flex-col gap-3`,children:[(0,I.jsx)(`p`,{className:`text-sm leading-relaxed text-muted`,children:`Cách làm trong lab THPT, và cách làm trong nhà máy nếu khác. Dòng “Trong app” chỉ bài để tự tay thấy hiện tượng.`}),prep.map(e=>(0,I.jsxs)(`article`,{className:`rounded-xl bg-surface p-4 shadow-[var(--shadow-border)]`,children:[(0,I.jsx)(`h2`,{className:`font-display text-base font-semibold`,children:e.name}),(0,I.jsx)(`p`,{className:`mt-1 text-sm leading-relaxed text-fg`,children:e.how}),e.eq.length?(0,I.jsx)(`div`,{className:`mt-2 flex flex-col gap-1`,children:e.eq.map(t=>(0,I.jsx)(`p`,{className:`font-mono text-sm text-fg`,children:t},t))}):null,(0,I.jsxs)(`p`,{className:`mt-2 text-sm leading-relaxed text-muted`,children:[`Công nghiệp: `,e.ind]}),(0,I.jsxs)(`p`,{className:`text-sm leading-relaxed text-muted`,children:[`Trong app: `,e.labs]})]},e.name))]}) :tab===`use`?(0,I.jsxs)(`div`,{className:`flex flex-col gap-3`,children:[(0,I.jsx)(`p`,{className:`text-sm leading-relaxed text-muted`,children:`Vài việc gặp ngoài đời, gắn với chất hoặc quá trình trong các bài. Không liệt kê cho đủ.`}),use.map(e=>(0,I.jsxs)(`article`,{className:`rounded-xl bg-surface p-4 shadow-[var(--shadow-border)]`,children:[(0,I.jsx)(`h2`,{className:`font-display text-base font-semibold`,children:e.name}),(0,I.jsx)(`div`,{className:`mt-2 flex flex-col gap-1`,children:e.uses.map(t=>(0,I.jsxs)(`p`,{className:`text-sm leading-relaxed text-fg`,children:[`· `,t]},t))}),(0,I.jsxs)(`p`,{className:`mt-2 text-sm leading-relaxed text-muted`,children:[`Trong app: `,e.labs]})]},e.name))]}) :(0,I.jsxs)(`section`,{className:`flex flex-col gap-3`,children:
""".replace("\n","")
rep(
"children:[`Dấu hiệu: `,e.sign]})]},e.name))]}) :(0,I.jsxs)(`section`,{className:`flex flex-col gap-3`,children:",
"children:[`Dấu hiệu: `,e.sign]})]},e.name))]}) :tab===`prep`?" + prep_view
)

rep(
"children:`Các loại phản ứng`}),(0,I.jsx)(`button`,{type:`button`,onClick:he,className:`inline-flex h-11 items-center rounded-md px-3 text-sm text-muted`,children:`Đã hiểu`})",
"children:`Các loại phản ứng`}),(0,I.jsx)(`button`,{type:`button`,onClick:()=>be(`prep`),className:`inline-flex h-11 items-center rounded-md bg-elevated px-3 text-sm text-fg shadow-[var(--shadow-border)]`,children:`Điều chế các chất`}),(0,I.jsx)(`button`,{type:`button`,onClick:()=>be(`use`),className:`inline-flex h-11 items-center rounded-md bg-elevated px-3 text-sm text-fg shadow-[var(--shadow-border)]`,children:`Ứng dụng thực tế`}),(0,I.jsx)(`button`,{type:`button`,onClick:he,className:`inline-flex h-11 items-center rounded-md px-3 text-sm text-muted`,children:`Đã hiểu`})"
)

rep(
"[`polime-nhiet`]:`Đun polime`})[e.id]),tipOn&&n===0?",
"[`polime-nhiet`]:`Đun polime`})[e.id]),(0,q.jsx)(`button`,{type:`button`,onClick:()=>{try{sessionStorage.setItem(`phong-basics`,`prep`)}catch{} goB(`basics`)},className:`w-fit rounded-full bg-elevated px-3 py-1 text-left text-xs text-muted`,children:`Điều chế / Ứng dụng`}),tipOn&&n===0?"
)

p.write_text(s, encoding="utf-8")
print("ok", p)
