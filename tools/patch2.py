# Vá index.html (bản minify) — một lần, trên file trước khi vá.
# Nhiệt theo bước, điện phân có hình, hai bài Hóa 12, câu hỏi và số đếm.
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
s = p.read_text(encoding="utf-8")

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:70], s.count(old))
    s = s.replace(old, new)

# Trình duyệt không còn xin favicon.ico (404 trong console).
rep(
'<title>Phòng Lab — Hóa học THPT</title>',
'<title>Phòng Lab — Hóa học THPT</title>\n    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 16 16\'%3E%3Crect width=\'16\' height=\'16\' rx=\'3\' fill=\'%231c1b18\'/%3E%3Cpath d=\'M6 2h4v3l3 6a3 3 0 0 1-2.6 4H5.6A3 3 0 0 1 3 11l3-6z\' fill=\'%23e07a4a\'/%3E%3C/svg%3E" />'
)

# 1. Đun: nhãn và kiểu lửa theo trường heat của bước (bath | gentle | direct).
rep(
"function gi({on:e,color:t=`#e07a4a`}){return(0,R.jsxs)(`div`,{className:`flex flex-col items-center`,children:[(0,R.jsx)(`div`,{className:`relative h-10 w-8`,children:e?(0,R.jsx)(`span`,{className:`absolute bottom-0 left-1/2 h-10 w-4 -translate-x-1/2 rounded-t-full`,style:{background:`linear-gradient(to top, ${t}, transparent)`,animation:`flame-flicker 0.7s ease-in-out infinite`,transformOrigin:`bottom center`}}):null}),(0,R.jsx)(`div`,{className:`h-8 w-6 rounded-b-sm bg-elevated shadow-[var(--shadow-border)]`}),(0,R.jsx)(`div`,{className:`h-1.5 w-10 rounded-full bg-faint`})]})}",
"function gi({on:e,mode:n,color:t=`#e07a4a`}){let r=n===`gentle`,i=n===`bath`;return(0,R.jsxs)(`div`,{className:`flex flex-col items-center`,children:[(0,R.jsx)(`div`,{className:`relative h-10 w-8`,children:e?(0,R.jsx)(`span`,{className:`absolute bottom-0 left-1/2 -translate-x-1/2 rounded-t-full`,style:{height:i?16:r?24:40,width:i?20:r?12:16,background:i?`radial-gradient(circle at 50% 80%, #8ec8d6, transparent 70%)`:`linear-gradient(to top, ${r?`#f0b27a`:t}, transparent)`,animation:`flame-flicker ${r?`1.15s`:`0.7s`} ease-in-out infinite`,transformOrigin:`bottom center`}}):null}),(0,R.jsx)(`div`,{className:`h-8 w-6 rounded-b-sm bg-elevated shadow-[var(--shadow-border)]`}),(0,R.jsx)(`div`,{className:`h-1.5 w-10 rounded-full bg-faint`}),n?(0,R.jsx)(`p`,{className:`mt-1 text-center text-[11px] text-muted`,children:i?`Cách thủy`:n===`direct`?`Lửa trực tiếp`:`Lửa nhỏ`}):null]})}"
)

rep(
"v.kind===`heat`?(0,q.jsx)(`div`,{className:`mt-4`,children:(0,q.jsxs)(Er,{onClick:te,variant:m?`primary`:`secondary`,children:[(0,q.jsx)(we,{className:`size-4`}),`Đun cách thủy`]})}):null",
"v.kind===`heat`?(0,q.jsx)(`div`,{className:`mt-4`,children:(0,q.jsxs)(Er,{onClick:te,variant:m?`primary`:`secondary`,children:[(0,q.jsx)(we,{className:`size-4`}),v.heat===`gentle`?`Đun nhẹ`:v.heat===`direct`?`Đun trực tiếp`:`Đun cách thủy`]})}):null"
)

rep(
"v.kind===`heat`||m?(0,q.jsx)(`div`,{className:`mt-3`,children:(0,q.jsx)(gi,{on:m})}):null",
"v.kind===`heat`||m?(0,q.jsx)(`div`,{className:`mt-3`,children:(0,q.jsx)(gi,{on:m,mode:e.steps.slice(0,n+1).reduce((t,r)=>r.kind===`heat`?r.heat||`bath`:t,`bath`)})}):null"
)

# Bước đun thứ hai trong cùng bài: tắt lửa khi vừa vào bước đó, bấm lại mới đun.
rep(
"function S(){if(ee(),_(null),y){i(e.id),delete Kn.runs[e.id],t();return}r(n+1)}",
"function S(){if(ee(),_(null),y){i(e.id),delete Kn.runs[e.id],t();return}e.steps[n+1]?.kind===`heat`&&h(!1),r(n+1)}"
)

# 2. Hình theo bước (visual trên step) + điện cực trên ống / bình.
rep(
"let x=(0,Is.useMemo)(()=>{if(g)return g;if(o.length>=2){let e=Ja(o,b);if(e.missing.length===0&&e.reaction)return e.reaction.visual}if(o.length){let e=o[o.length-1];return{liquid:(e?oi[e]?.color:void 0)??`#d5e0e4`,bubbles:o.includes(`hcl`)&&(o.includes(`zn`)||o.includes(`fe`)||o.includes(`mg`)||o.includes(`al`))}}return null},[o,m,g]);",
"let x=(0,Is.useMemo)(()=>{if(g)return g;let r=null;for(let t=0;t<e.steps.length;t++){let i=e.steps[t];i.visual&&(t<n||t===n&&u)&&(r=i.visual)}if(r)return r;if(o.length>=2){let e=Ja(o,b);if(e.missing.length===0&&e.reaction)return e.reaction.visual}if(o.length){let e=o[o.length-1];return{liquid:(e?oi[e]?.color:void 0)??`#d5e0e4`,bubbles:o.includes(`hcl`)&&(o.includes(`zn`)||o.includes(`fe`)||o.includes(`mg`)||o.includes(`al`))}}return null},[o,m,g,n,u,e]);"
)

rep(
"e.mirror?(0,R.jsx)(`rect`,{x:`20`,y:`40`,width:`20`,height:`3`,fill:`#f2f5f6`,opacity:`0.85`}):null]}):null",
"e.mirror?(0,R.jsx)(`rect`,{x:`20`,y:`40`,width:`20`,height:`3`,fill:`#f2f5f6`,opacity:`0.85`}):null,e.glow?(0,R.jsx)(`ellipse`,{cx:`30`,cy:`78`,rx:`8`,ry:`4`,fill:`rgba(255,255,255,0.35)`}):null]}):null"
)

rep(
"(0,R.jsx)(`rect`,{x:`16`,y:`10`,width:`28`,height:`8`,rx:`1`,fill:`none`,stroke:`rgba(235,238,233,0.4)`})]}),e?.bubbles?",
"(0,R.jsx)(`rect`,{x:`16`,y:`10`,width:`28`,height:`8`,rx:`1`,fill:`none`,stroke:`rgba(235,238,233,0.4)`}),e?.electrodes?(0,R.jsxs)(`g`,{children:[(0,R.jsx)(`rect`,{x:`24`,y:`30`,width:`2.2`,height:`68`,rx:`1`,fill:`#2a2a2a`}),(0,R.jsx)(`rect`,{x:`34`,y:`30`,width:`2.2`,height:`68`,rx:`1`,fill:`#2a2a2a`}),e.cathode?(0,R.jsx)(`rect`,{x:`22.4`,y:`68`,width:`5.4`,height:`30`,rx:`1.2`,fill:e.cathode}):null,e.anodeBubbles?[0,1,2].map(t=>(0,R.jsx)(`circle`,{cx:`37`,cy:78-t*10,r:`1.3`,fill:`rgba(255,255,255,0.85)`,style:{animation:`bubble 1.2s ease-out ${t*.22}s infinite`}},`b${t}`)):null]}):null]}),e?.bubbles?"
)

rep(
"e?.bubbles?(0,R.jsx)(`div`,{className:`pointer-events-none absolute inset-x-0 top-16 flex justify-center gap-0.5`,children:[0,1,2].map(e=>(0,R.jsx)(`span`,{className:`size-1 rounded-full bg-fg/70`,style:{animation:`bubble 1.2s ease-out ${e*.2}s infinite`}},e))}):null]})}function gi(",
"e?.bubbles?(0,R.jsx)(`div`,{className:`pointer-events-none absolute inset-x-0 top-16 flex justify-center gap-0.5`,children:[0,1,2].map(e=>(0,R.jsx)(`span`,{className:`size-1 rounded-full bg-fg/70`,style:{animation:`bubble 1.2s ease-out ${e*.2}s infinite`}},e))}):null,e?.smoke?(0,R.jsx)(`div`,{className:`pointer-events-none absolute top-2 left-1/2 flex -translate-x-1/2 gap-1`,children:[0,1,2].map(e=>(0,R.jsx)(`span`,{className:`h-8 w-3 rounded-full bg-fg/20`,style:{animation:`vapor 1.6s ease-out ${e*.3}s infinite`}},e))}):null]})}function gi("
)

rep(
"(0,R.jsx)(`path`,{d:`M50 22 v14`,stroke:`rgba(255,255,255,0.28)`,strokeWidth:`3`,strokeLinecap:`round`})]}),e?.smoke?",
"(0,R.jsx)(`path`,{d:`M50 22 v14`,stroke:`rgba(255,255,255,0.28)`,strokeWidth:`3`,strokeLinecap:`round`}),e?.electrodes?(0,R.jsxs)(`g`,{children:[(0,R.jsx)(`rect`,{x:`44`,y:`30`,width:`3`,height:`72`,rx:`1.2`,fill:`#2a2a2a`}),(0,R.jsx)(`rect`,{x:`73`,y:`30`,width:`3`,height:`72`,rx:`1.2`,fill:`#2a2a2a`}),e.cathode?(0,R.jsx)(`rect`,{x:`41.2`,y:`62`,width:`8.6`,height:`38`,rx:`2`,fill:e.cathode}):null,e.anodeBubbles?[0,1,2,3].map(t=>(0,R.jsx)(`circle`,{cx:`78`,cy:88-t*8,r:1.6+t%2*.4,fill:`rgba(255,255,255,0.85)`,style:{animation:`bubble ${1.15+t%2*.25}s ease-out ${t*.2}s infinite`}},`o${t}`)):null,(0,R.jsx)(`text`,{x:`45.5`,y:`26`,textAnchor:`middle`,fill:`rgba(235,238,233,0.75)`,fontSize:`8`,children:`−`}),(0,R.jsx)(`text`,{x:`74.5`,y:`26`,textAnchor:`middle`,fill:`rgba(235,238,233,0.75)`,fontSize:`8`,children:`+`})]}):null]}),e?.smoke?"
)

# 3. Kiểu đun của các bước cũ.
rep("kind:`heat`,prompt:`Đun cách thủy hỗn hợp vài phút.`", "kind:`heat`,heat:`bath`,prompt:`Đun cách thủy hỗn hợp vài phút.`")
rep("kind:`heat`,prompt:`Đun nhẹ ống trong nước ấm.`", "kind:`heat`,heat:`bath`,prompt:`Đun nhẹ ống trong nước ấm.`")
rep(
"kind:`heat`,prompt:`Đun sôi nhẹ 8–10 phút, khuấy đều, thỉnh thoảng thêm vài giọt nước cất.`",
"kind:`heat`,heat:`gentle`,prompt:`Đun sôi nhẹ 8–10 phút, khuấy đều, thỉnh thoảng thêm vài giọt nước cất.`"
)
rep(
"kind:`heat`,prompt:`Ngâm ống trong cốc nước nóng 60–70 °C vài phút, không lắc.`",
"kind:`heat`,heat:`bath`,prompt:`Ngâm ống trong cốc nước nóng 60–70 °C vài phút, không lắc.`"
)
rep(
"kind:`heat`,prompt:`Đun nóng nhẹ ống nghiệm (hướng miệng ống ra xa người).`",
"kind:`heat`,heat:`gentle`,prompt:`Đun nóng nhẹ ống nghiệm (hướng miệng ống ra xa người).`"
)

# 4. Điện phân CuSO4: xanh + điện cực, rồi đồng bám catot, bọt O2 ở anot, xanh nhạt.
rep(
"success:`Dung dịch xanh lam chứa Cu2+, SO4^2- và H2O.`,fail:`Chất điện phân ở bài này là CuSO4.`}",
"success:`Dung dịch xanh lam chứa Cu2+, SO4^2- và H2O.`,fail:`Chất điện phân ở bài này là CuSO4.`,visual:{liquid:`#3d7ec9`,electrodes:!0}}"
)
rep(
"note:`Catot (cực −): lớp đồng đỏ bám vào. Anot (cực +): bọt khí không màu (O2). Màu xanh nhạt dần vì Cu2+ giảm. Làm nơi thoáng, không dùng nguồn điện xoay chiều.`}",
"note:`Catot (cực −): lớp đồng đỏ bám vào. Anot (cực +): bọt khí không màu (O2). Màu xanh nhạt dần vì Cu2+ giảm. Làm nơi thoáng, không dùng nguồn điện xoay chiều.`,visual:{liquid:`#7eb0cc`,electrodes:!0,cathode:`#c4622d`,anodeBubbles:!0}}"
)

# 5. Hóa chất và phản ứng làm mềm nước cứng.
rep(
"{id:`kscn`,name:`Kali thioxianat`,formula:`KSCN`,kind:`salt`,color:`#eef2f4`,state:`solution`,hazard:`Độc khi gặp axit mạnh`}],oi=",
"{id:`kscn`,name:`Kali thioxianat`,formula:`KSCN`,kind:`salt`,color:`#eef2f4`,state:`solution`,hazard:`Độc khi gặp axit mạnh`},"
"{id:`cahco3`,name:`Nước cứng tạm thời`,formula:`Ca(HCO3)2`,kind:`salt`,color:`#d5e3ea`,state:`solution`},"
"{id:`pe`,name:`Polietilen (PE)`,formula:`(C2H4)n`,kind:`organic`,color:`#f3f4f2`,state:`solid`},"
"{id:`pvc`,name:`Poli(vinyl clorua)`,formula:`(C2H3Cl)n`,kind:`organic`,color:`#eceae4`,state:`solid`,hazard:`Đun nóng sinh HCl`}],oi="
)

rep(
"visual:{liquid:`#a8c4a0`}}],Qa=",
"visual:{liquid:`#a8c4a0`}},"
"{id:`cahco3-na2co3`,reagents:[`cahco3`,`na2co3`],type:`ket-tua`,typeLabel:`Làm mềm nước cứng`,equation:`Ca(HCO3)2 + Na2CO3 → CaCO3↓ + 2NaHCO3`,observation:`Kết tủa trắng CaCO3. Nước cứng tạm thời được làm mềm.`,products:`Canxi cacbonat và natri hiđrocacbonat.`,theory:`CO3^2- kết tủa Ca2+. Na2CO3 làm mềm cả nước cứng tạm thời và vĩnh cửu. Đun sôi chỉ làm mềm nước cứng tạm thời: Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O.`,grade:12,visual:{liquid:`#e7eef0`,ppt:`#f4f4f0`,pptLabel:`CaCO3`}}],Qa="
)

# 6. Hai bài thí nghiệm Hóa 12.
exps = r"""
,{id:`nuoc-cung`,title:`Làm mềm nước cứng tạm thời`,grade:12,minutes:8,visual:`tube`,aim:`Làm mềm nước cứng tạm thời bằng đun sôi và bằng Na2CO3, thu kết tủa CaCO3.`,materials:[`Dung dịch Ca(HCO3)2`,`Na2CO3`,`Ống nghiệm`,`Đèn cồn`],steps:[{id:`s1`,kind:`add`,reagentId:`cahco3`,prompt:`Cho khoảng 3 ml nước cứng tạm thời (Ca(HCO3)2) vào ống nghiệm.`,success:`Nước trong, chứa Ca2+ và HCO3-. Xà phòng với nước này ít bọt. Mẫu thường pha bằng cách thổi CO2 vào nước vôi trong đến khi kết tủa tan lại.`,fail:`Bài này bắt đầu bằng nước cứng tạm thời.`,visual:{liquid:`#d5e3ea`}},{id:`s2`,kind:`heat`,heat:`direct`,prompt:`Đun sôi trực tiếp trên đèn cồn 2–3 phút. Hướng miệng ống ra xa người, không đậy nút.`,success:`Có kết tủa trắng và bọt khí: Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O. Lọc bỏ CaCO3 thì nước bớt Ca2+. Đun sôi không làm mềm nước cứng vĩnh cửu (CaCl2, CaSO4).`,visual:{liquid:`#e4eef2`,ppt:`#f4f4f0`,pptLabel:`CaCO3`,bubbles:!0}},{id:`s3`,kind:`observe`,prompt:`Quan sát kết tủa trắng và khí thoát ra.`,note:`CaCO3 trắng, ít tan. Khí CO2 làm đục nước vôi trong. Ống còn nóng — kẹp ống, để nguội trước khi rót.`},{id:`s4`,kind:`add`,reagentId:`na2co3`,prompt:`Thêm khoảng 1 ml dung dịch Na2CO3.`,success:`Phần Ca(HCO3)2 còn lại cũng kết tủa: Ca(HCO3)2 + Na2CO3 → CaCO3↓ + 2NaHCO3. Na2CO3 làm mềm được cả nước cứng tạm thời và vĩnh cửu.`,fail:`Cần Na2CO3 để kết tủa Ca2+.`,visual:{liquid:`#e7eef2`,ppt:`#f7f7f4`,pptLabel:`CaCO3`}},{id:`s5`,kind:`choice`,prompt:`Đun sôi làm mềm được loại nước cứng nào?`,options:[`Chỉ nước cứng tạm thời`,`Chỉ nước cứng vĩnh cửu`,`Cả hai loại`,`Không loại nào`],correct:0,explain:`Tạm thời chứa HCO3-, bị nhiệt phân thành CaCO3. Vĩnh cửu chứa Cl- hoặc SO4^2-, đun sôi không kết tủa.`},{id:`s6`,kind:`choice`,prompt:`Phương trình nào đúng khi đun sôi Ca(HCO3)2?`,options:[`Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O`,`Ca(HCO3)2 → CaO + 2CO2 + H2O`,`CaCl2 → Ca↓ + Cl2`,`CaCO3 + H2O → Ca(OH)2 + CO2`],correct:0,explain:`Hiđrocacbonat nhiệt phân thành cacbonat ít tan, CO2 và nước. CaO chỉ thu được khi nung CaCO3 ở nhiệt độ rất cao.`},{id:`s7`,kind:`conclude`,summary:`Nước cứng tạm thời được làm mềm bằng đun sôi hoặc bằng Na2CO3; cả hai đều cho kết tủa CaCO3. Đun sôi không có tác dụng với nước cứng vĩnh cửu. Na2CO3 thì làm mềm được cả hai.`,equation:`Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O`}]}
,{id:`polime-nhiet`,title:`PE và PVC khi đun nóng`,grade:12,minutes:8,visual:`tube`,aim:`Thấy PE nhiệt dẻo khi đun nhẹ, và PVC phân hủy giải phóng HCl.`,materials:[`Hạt polietilen`,`Mẩu PVC`,`Ống nghiệm khô`,`Đèn cồn`,`Giấy quỳ ẩm`],steps:[{id:`s1`,kind:`add`,reagentId:`pe`,prompt:`Cho vài hạt polietilen vào ống nghiệm khô.`,success:`PE trùng hợp từ etilen, mạch chỉ có C và H, trắng đục, không tan trong nước.`,fail:`Bắt đầu với polietilen.`,visual:{liquid:`#f3f4f2`,ppt:`#f7f7f5`,pptLabel:`Hạt PE`}},{id:`s2`,kind:`heat`,heat:`gentle`,prompt:`Đun nhẹ trên đèn cồn, không đốt cháy mẫu. Kẹp ống, miệng ống hướng ra xa người.`,success:`PE chảy mềm, có thể kéo sợi; để nguội thì rắn lại và không hóa đen. Đó là polime nhiệt dẻo. Nếu đun cháy: ngọn lửa sáng, mùi nến — tắt ngay, làm nơi thoáng.`,visual:{liquid:`#f6f1e4`,glow:!0}},{id:`s3`,kind:`observe`,prompt:`Để ống nguội và quan sát PE rắn lại.`,note:`Không có khí làm quỳ ẩm đổi màu. PE không chứa clo.`},{id:`s4`,kind:`add`,reagentId:`pvc`,prompt:`Đổi sang ống khô khác: cho một mẩu PVC (ở bài này, thêm PVC vào ống).`,success:`PVC là poli(vinyl clorua), mắt xích –CH2–CHCl–. Chưa đun thì chưa có khí axit.`,fail:`Cần mẫu PVC.`,visual:{liquid:`#eceae4`,ppt:`#e4e0d8`,pptLabel:`PVC`}},{id:`s5`,kind:`heat`,heat:`gentle`,prompt:`Đun nhẹ mẩu PVC. Đưa giấy quỳ ẩm vào miệng ống, không hít khói.`,success:`PVC phân hủy, khói làm quỳ ẩm hóa đỏ: (–CH2–CHCl–)n → (–CH=CH–)n + nHCl. HCl độc — làm nơi thoáng, ngừng đun khi đã thấy khí.`,visual:{liquid:`#d9d3c6`,smoke:!0}},{id:`s6`,kind:`test`,testId:`litmus`,prompt:`Chạm giấy quỳ ẩm vào khói ở miệng ống.`,success:`Quỳ ẩm hóa đỏ: khí là HCl. PE đun nhẹ không cho phản ứng này.`,fail:`Dùng giấy quỳ ẩm để nhận ra HCl.`},{id:`s7`,kind:`choice`,prompt:`Đun nóng vừa phải rồi để nguội, polietilen`,options:[`Chảy mềm, nguội lại rắn (nhiệt dẻo)`,`Giải phóng HCl`,`Tan hết trong nước`,`Hóa than ngay, không chảy`],correct:0,explain:`PE không có clo. nCH2=CH2 → (–CH2–CH2–)n. Đun quá mạnh PE mới cháy, ngọn lửa sáng, có mùi parafin.`},{id:`s8`,kind:`choice`,prompt:`Khí làm giấy quỳ ẩm hóa đỏ khi đun PVC là`,options:[`HCl`,`Cl2`,`CO2`,`NH3`],correct:0,explain:`(–CH2–CHCl–)n → (–CH=CH–)n + nHCl. Không phải clo tự do. Khí độc, không hít.`},{id:`s9`,kind:`conclude`,summary:`PE đun nhẹ chảy mềm rồi rắn lại khi nguội (nhiệt dẻo), không giải phóng axit. PVC đun nóng tách HCl, quỳ ẩm hóa đỏ. Cả hai đều là polime trùng hợp, khác nilon (trùng ngưng).`,equation:`(–CH2–CHCl–)n → (–CH=CH–)n + nHCl`}]}
""".replace("\n", "")
rep(
"equation:`Fe3+ + 3SCN- → Fe(SCN)3`}]}]})),Ms=",
"equation:`Fe3+ + 3SCN- → Fe(SCN)3`}]}" + exps + "]})),Ms="
)

rep(
"hóa nâu.`}];function Fr",
"hóa nâu.`},{id:`nuoc-cung`,title:`Nước cứng tạm thời`,line:`Đun sôi ra CaCO3. Na2CO3 cũng kết tủa CaCO3, và làm mềm cả nước cứng vĩnh cửu.`},{id:`polime-nhiet`,title:`PE và PVC`,line:`PE đun nhẹ thì mềm. PVC đun ra HCl, quỳ ẩm hóa đỏ.`}];function Fr"
)

# 7. Câu hỏi sổ tay và số đếm.
rep(
"explain:`Fe3+ + 3SCN- → Fe(SCN)3 màu đỏ máu.`}]},{id:`amin-polime`",
"explain:`Fe3+ + 3SCN- → Fe(SCN)3 màu đỏ máu.`},{id:`kl-6`,prompt:`Đun sôi nước cứng tạm thời, kết tủa thu được là`,options:[`CaCO3`,`Ca(OH)2`,`CaCl2`,`CaO`],correct:0,explain:`Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O. Đun sôi không kết tủa CaCl2 hay CaSO4 của nước cứng vĩnh cửu.`},{id:`kl-7`,prompt:`Cho Na2CO3 vào nước cứng tạm thời, phương trình đúng là`,options:[`Ca(HCO3)2 + Na2CO3 → CaCO3↓ + 2NaHCO3`,`Ca(HCO3)2 + Na2CO3 → CaO + 2NaHCO3 + CO2`,`CaCO3 + Na2CO3 → Ca(HCO3)2`,`Ca(HCO3)2 → Ca + 2CO2 + H2`],correct:0,explain:`CO3^2- kết tủa Ca2+. Với nước cứng vĩnh cửu: CaCl2 + Na2CO3 → CaCO3↓ + 2NaCl.`}]},{id:`amin-polime`"
)
rep(
"Trùng hợp: monome có liên kết bội hoặc vòng kém bền (PE, PVC, PS, cao su buna).",
"Trùng hợp: monome có liên kết bội hoặc vòng kém bền (PE, PVC, PS, cao su buna). PE đun nóng chảy mềm, để nguội rắn lại (nhiệt dẻo). PVC đun nóng giải phóng HCl, giấy quỳ ẩm hóa đỏ."
)
rep(
"NaCl không phản ứng.`}]}]})),ic=",
"NaCl không phản ứng.`},{id:`ap-5`,prompt:`Đun nóng vừa phải polietilen rồi để nguội thì`,options:[`Chảy mềm, nguội lại rắn (nhiệt dẻo)`,`Giải phóng HCl làm quỳ hóa đỏ`,`Tan trong nước thành dung dịch`,`Hóa thành than ngay, không chảy`],correct:0,explain:`PE không có clo. Mạch (–CH2–CH2–)n mềm khi nóng và giữ hình dạng mới khi nguội. Đun cháy mới có ngọn lửa sáng, mùi nến.`},{id:`ap-6`,prompt:`Khí làm giấy quỳ ẩm hóa đỏ khi đun PVC là`,options:[`HCl`,`Cl2`,`CO2`,`NH3`],correct:0,explain:`(–CH2–CHCl–)n → (–CH=CH–)n + nHCl. HCl độc, làm nơi thoáng, không hít khói.`}]}]})),ic="
)

rep(
"En={reactions:97,experiments:16,questions:43}",
"En={reactions:98,experiments:18,questions:47}"
)

p.write_text(s, encoding="utf-8")
print("ok", p)
