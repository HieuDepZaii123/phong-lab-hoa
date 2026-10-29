# Vá index.html (bản minify) — một lần, trên file trước khi vá.
# Hướng dẫn người mới, Kiến thức cơ bản, Các loại phản ứng.
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
s = p.read_text(encoding="utf-8")

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:70], s.count(old))
    s = s.replace(old, new)

# 1. Bỏ thanh "khung xem trước không lưu được file".
rep(
"""    <div id="save-lab" style="position:sticky;top:0;z-index:99999;display:flex;gap:10px;align-items:center;justify-content:space-between;padding:10px 12px;background:#1c1b18;color:#f2efe8;font:14px/1.35 system-ui,sans-serif">
      <span>Khung xem trước không cho lưu file. Hãy tải thẻ phong-lab.zip trong cuộc trò chuyện.</span>
      <button id="save-lab-btn" type="button" style="flex:none;border:0;border-radius:8px;background:#f2efe8;color:#1c1b18;font:600 14px system-ui;padding:10px 14px">Đã hiểu</button>
    </div>
    <script>
      document.getElementById("save-lab-btn").onclick = async () => { document.getElementById("save-lab").querySelector("span").textContent = "File chỉ tải được từ thẻ phong-lab.zip trong cuộc trò chuyện, không phải từ khung này."; return;
        const btn = document.getElementById("save-lab-btn");
        const old = btn.textContent;
        btn.textContent = "Đang lưu…";
        try {
          const blob = await (await fetch(location.href)).blob();
          const file = new File([blob], "phong-lab.html", { type: "text/html" });
          if (navigator.canShare && navigator.canShare({ files: [file] })) {
            await navigator.share({ files: [file], title: "Phòng Lab" });
            btn.textContent = "Đã mở bảng lưu";
            return;
          }
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = "phong-lab.html";
          document.body.appendChild(a);
          a.click();
          a.remove();
          setTimeout(() => URL.revokeObjectURL(url), 2000);
          btn.textContent = "Nếu chưa về máy, dùng menu trình duyệt → Lưu trang";
        } catch (e) {
          if (e && e.name === "AbortError") { btn.textContent = old; return; }
          btn.textContent = "Khung này chặn lưu. Mở trang ra tab trình duyệt rồi Lưu trang";
        }
      };
    </script>
    <div id="app"></div>""",
"""    <div id="app"></div>"""
)

# 2. Trạm Kiến thức cơ bản + các loại phản ứng.
panel = r"""
function Yc({className:e}){return(0,I.jsxs)(`svg`,{viewBox:`0 0 24 24`,fill:`none`,stroke:`currentColor`,strokeWidth:`2`,strokeLinecap:`round`,strokeLinejoin:`round`,className:e,"aria-hidden":!0,children:[(0,I.jsx)(`path`,{d:`M4 19.5A2.5 2.5 0 0 1 6.5 17H20`}),(0,I.jsx)(`path`,{d:`M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z`})]})}
function Qc(){let[tab,setTab]=(0,jr.useState)(()=>{try{let e=sessionStorage.getItem(`phong-basics`);return e===`rx`||e===`tools`||e===`see`||e===`eq`||e===`grade`?e:`safe`}catch{return`safe`}});(0,jr.useEffect)(()=>{try{sessionStorage.removeItem(`phong-basics`)}catch{}},[]);let tabs=[[`safe`,`An toàn`],[`tools`,`Dụng cụ`],[`see`,`Hiện tượng`],[`eq`,`Phương trình`],[`grade`,`Theo lớp`],[`rx`,`Các loại phản ứng`]],primers={safe:{title:`An toàn phòng thí nghiệm`,lead:`Đây là lab ảo. Khi làm thật, luôn có giáo viên, kính và nơi thoáng.`,items:[[`Kính, găng`,`NaOH đặc, H2SO4 đặc và AgNO3 làm tổn thương da, mắt.`],[`Khi đun`,`Hướng miệng ống ra xa người. Không đậy nút.`],[`Khói độc`,`Đun PVC sinh HCl. Thuốc thử tráng bạc đổ bỏ sau bài, không để lâu.`],[`Không nếm`,`Không thử hóa chất bằng miệng.`]]},tools:{title:`Dụng cụ trên màn hình`,lead:`Mỗi nút là một thao tác. Đọc câu hỏi của bước rồi bấm đúng nút đó.`,items:[[`Ống nghiệm`,`Bài nhỏ: thêm hóa chất, đun, xem màu.`],[`Bình hoặc cốc`,`Điện phân CuSO4 và một số bài pha.`],[`Nút Đun`,`Ba kiểu: Đun cách thủy (không lửa trực tiếp), Đun nhẹ (lửa nhỏ), Đun trực tiếp (lửa lớn).`],[`Phép thử`,`Que đóm, giấy quỳ, nước vôi trong — chỉ bấm phép thử bài đang hỏi.`]]},see:{title:`Hiện tượng cần ghi`,lead:`Kết luận của từng bài nằm ở bước cuối. Phần này chỉ là cách nhìn.`,items:[[`Màu`,`Dung dịch đổi màu, hoặc mất màu thuốc thử (KMnO4 tím, nước brom).`],[`Kết tủa`,`Chất rắn xuất hiện: trắng, xanh, nâu đỏ, đỏ gạch. Có tủa tan khi thêm dư.`],[`Khí`,`Bọt khí, mùi, làm đục nước vôi (CO2), hoặc que đóm nổ nhẹ (H2).`],[`Chỉ thị`,`Phenolphtalein hồng trong bazơ, mất hồng khi axit đủ. Quỳ ẩm hóa đỏ với HCl.`]]},eq:{title:`Cách đọc phương trình`,lead:`Đối chiếu phương trình ở bước kết luận với hiện tượng vừa thấy.`,items:[[`Mũi tên`,`→ là một chiều. ⇌ là thuận nghịch, như este hóa.`],[`Ký hiệu`,`↓ là kết tủa. ↑ là khí thoát ra.`],[`Hệ số`,`Số đứng trước công thức là số mol tỉ lệ. Dùng cho câu tính trong bài.`],[`Cân bằng`,`Đếm nguyên tử hai vế. Thiếu hệ số thì phương trình chưa đúng.`]]},grade:{title:`Nên làm theo lớp`,lead:`Không cần thuộc hết trước. Lớp 10 trước, rồi mở rộng.`,items:[[`Lớp 10`,`Điều chế hidro, trung hòa, nhận biết ion. Thấy khí, màu, kết tủa ngay.`],[`Lớp 11`,`Anken với nước brom, este hóa, tráng gương, phenol.`],[`Lớp 12`,`Kim loại, điện phân, glucozơ, protein, nước cứng, PE/PVC.`]]}},rx=[{name:`Trao đổi`,def:`Hai hợp chất trao ion. Thường tạo kết tủa, khí hoặc nước.`,eq:[`AgNO3 + NaCl → AgCl↓ + NaNO3`,`Na2CO3 + 2HCl → 2NaCl + CO2↑ + H2O`],labs:`Nhận biết Cl-, SO4^2- và CO3^2-.`,sign:`Kết tủa trắng, hoặc sủi bọt. CO2 làm đục nước vôi trong.`},{name:`Trung hòa (axit–bazơ)`,def:`Axit phản ứng với bazơ cho muối và nước.`,eq:[`HCl + NaOH → NaCl + H2O`],labs:`Phản ứng trung hòa có phenolphtalein.`,sign:`Hồng của bazơ nhạt dần rồi mất khi vừa hết bazơ. Tỏa nhiệt nhẹ.`},{name:`Thế`,def:`Đơn chất hoạt động hơn đẩy đơn chất yếu hơn ra khỏi hợp chất.`,eq:[`Zn + 2HCl → ZnCl2 + H2↑`,`Fe + CuSO4 → FeSO4 + Cu`],labs:`Điều chế khí hidro.`,sign:`Sủi khí không màu. Que đóm trên miệng ống có tiếng nổ nhẹ với H2.`},{name:`Oxi hóa – khử`,def:`Có chất nhường electron và chất nhận electron. Số oxi hóa thay đổi.`,eq:[`MnO4- + 5Fe2+ + 8H+ → Mn2+ + 5Fe3+ + 4H2O`,`Zn + Cu2+ → Zn2+ + Cu`],labs:`KMnO4 oxi hóa Fe2+. Pin Daniell Zn–Cu cũng là oxi hóa–khử tự xảy ra, khác điện phân.`,sign:`Mất màu tím trong axit. Pin: kẽm mòn, đồng bám cực kia.`},{name:`Nhiệt phân`,def:`Nhiệt làm một chất tách thành chất đơn giản hơn.`,eq:[`Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O`],labs:`Làm mềm nước cứng tạm thời. Đun sôi chỉ có tác dụng với HCO3-, không với CaCl2.`,sign:`Cần đun. Kết tủa trắng và khí CO2.`},{name:`Điện phân`,def:`Dòng điện một chiều buộc phản ứng xảy ra. Catot (−) là cực khử, anot (+) là cực oxi hóa.`,eq:[`2CuSO4 + 2H2O → 2Cu + O2↑ + 2H2SO4`],labs:`Điện phân dung dịch CuSO4, điện cực trơ.`,sign:`Đồng đỏ bám catot, bọt O2 ở anot, màu xanh nhạt dần, dung dịch hóa axit.`},{name:`Cộng vào nối bội`,def:`Phân tử brom cộng vào liên kết đôi của anken, không cần ánh sáng.`,eq:[`C2H4 + Br2 → CH2Br–CH2Br`],labs:`Nhận biết anken bằng nước brom.`,sign:`Nước brom đỏ nâu mất màu.`},{name:`Este hóa và xà phòng hóa`,def:`Este hóa là axit + ancol, thuận nghịch, cần H2SO4 và đun cách thủy. Xà phòng hóa là este + NaOH, một chiều.`,eq:[`CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O`,`(C17H33COO)3C3H5 + 3NaOH → 3C17H33COONa + C3H5(OH)3`],labs:`Điều chế etyl axetat. Xà phòng hóa chất béo.`,sign:`Este có mùi thơm. Xà phòng: đun cho hỗn hợp đồng nhất, NaCl bão hòa đẩy lớp rắn nổi.`},{name:`Tráng bạc và khử Cu(OH)2`,def:`Nhóm –CHO khử Ag+ hoặc Cu2+ khi đun. Nhiều nhóm –OH kề nhau hòa tan Cu(OH)2 ngay khi lạnh.`,eq:[`C6H12O6 + 2[Ag(NH3)2]OH → C6H12O7 + 2Ag↓ + 4NH3 + H2O`],labs:`Tráng gương, tráng bạc của glucozơ, glucozơ với Cu(OH)2. Saccarozơ không tráng bạc nếu chưa thủy phân.`,sign:`Gương bạc khi đun cách thủy. Lạnh: dung dịch xanh lam. Đun: Cu2O đỏ gạch.`},{name:`Lưỡng tính`,def:`Al(OH)3 tan trong axit và trong kiềm dư. Muốn giữ kết tủa thì dùng NH3, không dùng NaOH dư.`,eq:[`AlCl3 + 3NaOH → Al(OH)3↓ + 3NaCl`,`Al(OH)3 + NaOH → Na[Al(OH)4]`],labs:`Tính lưỡng tính của nhôm.`,sign:`Kết tủa keo trắng, rồi tan nếu nhỏ tiếp NaOH.`},{name:`Phản ứng màu hữu cơ`,def:`Một số hợp chất cho màu với thuốc thử, không cần đun.`,eq:[`Protein + Cu(OH)2 / OH- → phức tím`,`Phenol + FeCl3 → phức tím`],labs:`Phản ứng biure của protein. Nhận biết phenol. Đipeptit không cho màu biure.`,sign:`Tím. Nhỏ quá nhiều CuSO4 thì tủa xanh che mất màu tím.`},{name:`Đun polime`,def:`PE đun nhẹ chỉ chảy mềm rồi rắn lại — không phải phản ứng hóa học. PVC đun thì tách HCl.`,eq:[`(–CH2–CHCl–)n → (–CH=CH–)n + nHCl`],labs:`PE và PVC khi đun nóng.`,sign:`PE mềm, nguội thì cứng trở lại, quỳ không đổi. PVC có khói làm quỳ ẩm hóa đỏ. Làm nơi thoáng.`}];return(0,I.jsxs)(`div`,{className:`flex flex-col gap-4`,children:[(0,I.jsxs)(`header`,{children:[(0,I.jsx)(`h1`,{className:`font-display text-2xl font-semibold tracking-tight`,children:`Kiến thức cơ bản`}),(0,I.jsx)(`p`,{className:`mt-1 max-w-2xl text-sm leading-relaxed text-muted`,children:`Nền ngắn trước khi vào bài: chọn bài lớp 10, làm từng bước, xem hiện tượng, rồi trả lời câu hỏi. Phần kết luận đầy đủ vẫn nằm trong từng thí nghiệm.`})]}),(0,I.jsx)(`div`,{className:`flex flex-wrap gap-2`,children:tabs.map(([e,t])=>(0,I.jsx)(`button`,{type:`button`,onClick:()=>setTab(e),className:e===tab?`inline-flex h-10 items-center rounded-full bg-accent px-3 text-sm font-medium text-accent-fg`:`inline-flex h-10 items-center rounded-full bg-elevated px-3 text-sm text-fg`,children:t},e))}),tab===`rx`?(0,I.jsxs)(`div`,{className:`flex flex-col gap-3`,children:[(0,I.jsx)(`p`,{className:`text-sm leading-relaxed text-muted`,children:`Mỗi loại dưới đây gắn với bài đang có trong lab. Bấm chip “Loại phản ứng” trong một bài để mở lại trang này.`}),rx.map(e=>(0,I.jsxs)(`article`,{className:`rounded-xl bg-surface p-4 shadow-[var(--shadow-border)]`,children:[(0,I.jsx)(`h2`,{className:`font-display text-base font-semibold`,children:e.name}),(0,I.jsx)(`p`,{className:`mt-1 text-sm leading-relaxed text-fg`,children:e.def}),(0,I.jsx)(`div`,{className:`mt-2 flex flex-col gap-1`,children:e.eq.map(t=>(0,I.jsx)(`p`,{className:`font-mono text-sm text-fg`,children:t},t))}),(0,I.jsxs)(`p`,{className:`mt-2 text-sm leading-relaxed text-muted`,children:[`Trong app: `,e.labs]}),(0,I.jsxs)(`p`,{className:`text-sm leading-relaxed text-muted`,children:[`Dấu hiệu: `,e.sign]})]},e.name))]}) :(0,I.jsxs)(`section`,{className:`flex flex-col gap-3`,children:[(0,I.jsx)(`h2`,{className:`font-display text-lg font-semibold`,children:primers[tab].title}),(0,I.jsx)(`p`,{className:`text-sm leading-relaxed text-muted`,children:primers[tab].lead}),primers[tab].items.map(([e,t])=>(0,I.jsxs)(`div`,{className:`rounded-lg bg-surface p-3 shadow-[var(--shadow-border)]`,children:[(0,I.jsx)(`p`,{className:`text-sm font-semibold`,children:e}),(0,I.jsx)(`p`,{className:`mt-1 text-sm leading-relaxed text-muted`,children:t})]},e))]})]})}
""".replace("\n","")
rep(
"vc={lobby:Ne,bench:de,periodic:Ae,experiments:De,titration:ve,notebook:A},yc={bench:pc,periodic:mc,experiments:hc,titration:gc,notebook:_c},bc=[`lobby`,`bench`,`periodic`,`experiments`,`notebook`]",
"vc={lobby:Ne,bench:de,periodic:Ae,experiments:De,titration:ve,notebook:A,basics:Yc},yc={bench:pc,periodic:mc,experiments:hc,titration:gc,notebook:_c,basics:Qc},bc=[`lobby`,`bench`,`periodic`,`experiments`,`basics`,`notebook`]"
)
rep(
"{id:`experiments`,label:`Bài thí nghiệm`,short:`Bài TN`,hint:`Thí nghiệm theo SGK`},{id:`titration`",
"{id:`experiments`,label:`Bài thí nghiệm`,short:`Bài TN`,hint:`Thí nghiệm theo SGK`},{id:`basics`,label:`Kiến thức cơ bản`,short:`Cơ bản`,hint:`An toàn, dụng cụ, loại phản ứng`},{id:`titration`"
)
rep(
"className:`grid grid-cols-5`,children:bc.map",
"className:`grid grid-cols-6`,children:bc.map"
)

# 3. Nút Hướng dẫn + lớp phủ lần đầu.
rep(
"function xc(){let e=F(e=>e.station),t=F(e=>e.setStation),n=F(e=>e.discovered),r=yc[e];return",
panel+"function xc(){let e=F(e=>e.station),t=F(e=>e.setStation),n=F(e=>e.discovered),r=yc[e],[ae,oe]=(0,jr.useState)(()=>{try{return localStorage.getItem(`phong-lab-help-v1`)!==`1`}catch{return!0}});function he(){try{localStorage.setItem(`phong-lab-help-v1`,`1`)}catch{} oe(!1)}function be(e){try{sessionStorage.setItem(`phong-basics`,e)}catch{} t(`basics`),he()}return"
)
rep(
"(0,I.jsxs)(`div`,{className:`hidden font-mono text-[11px] tabular-nums text-muted sm:block`,children:[n.length,`/`,En.reactions,` phản ứng`]})",
"(0,I.jsx)(`button`,{type:`button`,onClick:()=>oe(!0),className:`inline-flex h-10 shrink-0 items-center rounded-md px-2.5 text-sm text-fg hover:bg-elevated`,children:`Hướng dẫn`}),(0,I.jsxs)(`div`,{className:`hidden font-mono text-[11px] tabular-nums text-muted sm:block`,children:[n.length,`/`,En.reactions,` phản ứng`]})"
)
help = r"""
ae?(0,I.jsxs)(`div`,{className:`fixed inset-0 flex items-end justify-center p-3 sm:items-center`,style:{zIndex:70,background:`rgba(0,0,0,.55)`},children:[(0,I.jsx)(`button`,{type:`button`,"aria-label":`Đóng hướng dẫn`,className:`absolute inset-0`,onClick:he}),(0,I.jsxs)(`div`,{role:`dialog`,"aria-modal":!0,"aria-labelledby":`phong-help-title`,className:`relative w-full max-w-lg overflow-y-auto rounded-xl bg-surface p-4 shadow-[var(--shadow-border)] sm:p-5`,style:{maxHeight:`min(85vh,640px)`},children:[(0,I.jsx)(`p`,{className:`text-[11px] font-medium uppercase tracking-[0.16em] text-accent`,children:`Lần đầu vào lab`}),(0,I.jsx)(`h2`,{id:`phong-help-title`,className:`mt-1 font-display text-xl font-semibold tracking-tight`,children:`Bắt đầu trong 4 bước`}),(0,I.jsxs)(`ol`,{className:`mt-3 flex flex-col gap-2 text-sm leading-relaxed`,children:[(0,I.jsx)(`li`,{children:`1. Chọn bài thí nghiệm. Người mới nên làm ba bài lớp 10 trước.`}),(0,I.jsx)(`li`,{children:`2. Làm đúng thao tác trên màn hình: thêm hóa chất, đun, hoặc quan sát.`}),(0,I.jsx)(`li`,{children:`3. Nhìn hiện tượng: màu, khí, kết tủa. Đọc dòng lab ghi lại.`}),(0,I.jsx)(`li`,{children:`4. Trả lời câu hỏi cuối bài. Muốn nền trước, mở Kiến thức cơ bản hoặc Các loại phản ứng.`})]}),(0,I.jsxs)(`div`,{className:`mt-4 flex flex-wrap gap-2`,children:[(0,I.jsx)(`button`,{type:`button`,onClick:()=>{t(`experiments`),he()},className:`inline-flex h-11 items-center rounded-md bg-accent px-3 text-sm font-medium text-accent-fg`,children:`Bắt đầu thí nghiệm`}),(0,I.jsx)(`button`,{type:`button`,onClick:()=>be(`safe`),className:`inline-flex h-11 items-center rounded-md bg-elevated px-3 text-sm text-fg shadow-[var(--shadow-border)]`,children:`Kiến thức cơ bản`}),(0,I.jsx)(`button`,{type:`button`,onClick:()=>be(`rx`),className:`inline-flex h-11 items-center rounded-md bg-elevated px-3 text-sm text-fg shadow-[var(--shadow-border)]`,children:`Các loại phản ứng`}),(0,I.jsx)(`button`,{type:`button`,onClick:he,className:`inline-flex h-11 items-center rounded-md px-3 text-sm text-muted`,children:`Đã hiểu`})]})]})]}):null
""".replace("\n","")
rep(
"r.short]})},n)})})})]})}",
"r.short]})},n)})})}),"+help+"]})}"
)

# 4. Sảnh: lời dẫn và nút rõ.
rep("children:`Ca trực hôm nay`", "children:`Bài gợi ý hôm nay`")
rep(
"(0,I.jsxs)(Er,{onClick:()=>c(s.id),children:[`Làm ca này`,(0,I.jsx)(O,{className:`size-4`})]}),(0,I.jsx)(Er,{variant:`secondary`,onClick:()=>t(`identify`),children:`Nhận biết mẫu lạ`})",
"(0,I.jsx)(Er,{onClick:()=>e(`experiments`),children:`Chọn bài thí nghiệm`}),(0,I.jsx)(Er,{variant:`secondary`,onClick:()=>c(s.id),children:`Làm bài gợi ý`}),(0,I.jsx)(Er,{variant:`secondary`,onClick:()=>e(`basics`),children:`Kiến thức cơ bản`}),(0,I.jsx)(Er,{variant:`secondary`,onClick:()=>t(`identify`),children:`Nhận biết mẫu lạ`})"
)
rep(
"children:s.line}),(0,I.jsxs)(`div`,{className:`mt-4 flex flex-wrap gap-2`",
"children:s.line}),(0,I.jsx)(`p`,{className:`mt-3 max-w-lg text-sm leading-relaxed text-fg`,children:`Người mới: bấm Chọn bài thí nghiệm, làm lần lượt từng bước, rồi xem màu, khí hoặc kết tủa.`}),(0,I.jsxs)(`div`,{className:`mt-4 flex flex-wrap gap-2`"
)

# 5. Danh sách bài: ba bài lớp 10.
starters = r"""
(0,q.jsxs)(`section`,{className:`rounded-xl bg-elevated p-4`,children:[(0,q.jsx)(`p`,{className:`text-[11px] font-medium uppercase tracking-[0.16em] text-accent`,children:`Bắt đầu từ đây`}),(0,q.jsx)(`p`,{className:`mt-1 text-sm leading-relaxed text-muted`,children:`Ba bài lớp 10, ngắn, dễ thấy khí hoặc màu. Làm xong một bước thì bấm Bước tiếp.`}),(0,q.jsxs)(`div`,{className:`mt-3 flex flex-col gap-2`,children:[(0,q.jsxs)(`button`,{type:`button`,onClick:()=>t(`dieu-che-h2`),className:`flex min-h-11 w-full items-center justify-between rounded-lg bg-surface px-3 py-2 text-left shadow-[var(--shadow-border)]`,children:[(0,q.jsxs)(`span`,{children:[(0,q.jsx)(`span`,{className:`block text-sm font-semibold`,children:`Điều chế khí hidro`}),(0,q.jsx)(`span`,{className:`block text-xs text-muted`,children:`Kẽm và axit, thử que đóm`})]}),(0,q.jsx)(`span`,{className:`text-sm text-accent`,children:`Làm`})]}),(0,q.jsxs)(`button`,{type:`button`,onClick:()=>t(`trung-hoa`),className:`flex min-h-11 w-full items-center justify-between rounded-lg bg-surface px-3 py-2 text-left shadow-[var(--shadow-border)]`,children:[(0,q.jsxs)(`span`,{children:[(0,q.jsx)(`span`,{className:`block text-sm font-semibold`,children:`Phản ứng trung hòa`}),(0,q.jsx)(`span`,{className:`block text-xs text-muted`,children:`HCl, NaOH và phenolphtalein`})]}),(0,q.jsx)(`span`,{className:`text-sm text-accent`,children:`Làm`})]}),(0,q.jsxs)(`button`,{type:`button`,onClick:()=>t(`nhan-biet-ion`),className:`flex min-h-11 w-full items-center justify-between rounded-lg bg-surface px-3 py-2 text-left shadow-[var(--shadow-border)]`,children:[(0,q.jsxs)(`span`,{children:[(0,q.jsx)(`span`,{className:`block text-sm font-semibold`,children:`Nhận biết ion`}),(0,q.jsx)(`span`,{className:`block text-xs text-muted`,children:`Kết tủa trắng và khí CO2`})]}),(0,q.jsx)(`span`,{className:`text-sm text-accent`,children:`Làm`})]})]})]}),
""".replace("\n","")
rep(
"không bỏ qua.`})]}),(0,q.jsxs)(`ul`,{className:`grid gap-3 sm:grid-cols-2`,children:",
"không bỏ qua.`})]}),"+starters+"(0,q.jsxs)(`ul`,{className:`grid gap-3 sm:grid-cols-2`,children:"
)

# 6. Trong bài: gợi ý một lần + chip loại phản ứng.
rep(
"[g,_]=(0,Is.useState)(a?.spill??null),v=e.steps[n]",
"[g,_]=(0,Is.useState)(a?.spill??null),[tipOn,setTipOn]=(0,Is.useState)(()=>{try{return localStorage.getItem(`phong-lab-coach`)!==`1`}catch{return!0}}),goB=F(e=>e.setStation),v=e.steps[n]"
)
coach = r"""
(n=>{return n?(0,q.jsx)(`button`,{type:`button`,onClick:()=>{try{sessionStorage.setItem(`phong-basics`,`rx`)}catch{} goB(`basics`)},className:`w-fit rounded-full bg-elevated px-3 py-1 text-left text-xs text-muted`,children:`Loại phản ứng: `+n+` · giải thích`},n):null})(({[`dieu-che-h2`]:`Thế`,[`trung-hoa`]:`Trung hòa`,[`nhan-biet-ion`]:`Trao đổi`,[`anken-brom`]:`Cộng nối bội`,[`este-hoa`]:`Este hóa`,[`pin-daniell`]:`Oxi hóa – khử (pin)`,[`luong-tinh-al`]:`Lưỡng tính`,[`kmno4-fe2`]:`Oxi hóa – khử`,[`nhan-biet-phenol`]:`Phản ứng màu`,[`trang-guong`]:`Tráng bạc`,[`xa-phong-hoa`]:`Xà phòng hóa`,[`trang-bac-glucozo`]:`Tráng bạc`,[`glucozo-cuoh2`]:`Khử Cu(OH)2`,[`biure-protein`]:`Phản ứng màu`,[`dien-phan-cuso4`]:`Điện phân`,[`nhan-biet-fe2-fe3`]:`Nhận biết ion`,[`nuoc-cung`]:`Nhiệt phân`,[`polime-nhiet`]:`Đun polime`})[e.id]),tipOn&&n===0?(0,q.jsxs)(`p`,{className:`rounded-lg bg-elevated px-3 py-2 text-sm leading-relaxed text-muted`,children:[`Chọn đúng hóa chất hoặc nút được hỏi. Xong bước thì bấm Bước tiếp. `,(0,q.jsx)(`button`,{type:`button`,className:`font-semibold text-accent`,onClick:()=>{try{localStorage.setItem(`phong-lab-coach`,`1`)}catch{} setTipOn(!1)},children:`Đã rõ`})]}):null,
""".replace("\n","")
rep(
"children:e.title}),(0,q.jsxs)(Ur,{children:[`Bước `,n+1,`/`,e.steps.length]})]}),(0,q.jsx)(`div`,{className:`h-1 overflow-hidden rounded-full bg-elevated`",
"children:e.title}),(0,q.jsxs)(Ur,{children:[`Bước `,n+1,`/`,e.steps.length]})]}),"+coach+"(0,q.jsx)(`div`,{className:`h-1 overflow-hidden rounded-full bg-elevated`"
)

p.write_text(s, encoding="utf-8")
print("ok", p)
