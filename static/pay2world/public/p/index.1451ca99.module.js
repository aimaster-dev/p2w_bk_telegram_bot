var D1 = Object.freeze,
    z1 = Object.defineProperty;
var C5 = (e, n, i) => n in e ? z1(e, n, {
    enumerable: !0,
    configurable: !0,
    writable: !0,
    value: i
}) : e[n] = i;
var U1 = (e, n, i) => (C5(e, typeof n != "symbol" ? n + "" : n, i), i);
var k = (e, n) => D1(z1(e, "raw", {
    value: D1(n || e.slice())
}));
import {
    i as a5,
    a as r5,
    n as V,
    j as t,
    I as n1,
    r as p,
    u as u1,
    b as Z,
    B as u,
    T as L,
    c as c5,
    p as l5,
    d as _1,
    e as d1,
    P as X,
    L as e1,
    f as U,
    g as p5,
    h as j,
    k as K1,
    l as u5,
    m as d5,
    o as A,
    q as h5,
    s as m5,
    t as V1,
    v as x1,
    w as P2,
    Q as b5,
    A as g5,
    x as N5,
    S as k5,
    y as V5,
    z as A5,
    R as C1,
    C as f5,
    D as B5
} from "./vendor.f16ec030.module.js";

function c6() {
    import.meta.url, import("_").catch(() => 1);
    async function* e() {}
}(function() {
    const n = document.createElement("link").relList;
    if (n && n.supports && n.supports("modulepreload")) return;
    for (const r of document.querySelectorAll('link[rel="modulepreload"]')) C(r);
    new MutationObserver(r => {
        for (const a of r)
            if (a.type === "childList")
                for (const s of a.addedNodes) s.tagName === "LINK" && s.rel === "modulepreload" && C(s)
    }).observe(document, {
        childList: !0,
        subtree: !0
    });

    function i(r) {
        const a = {};
        return r.integrity && (a.integrity = r.integrity), r.referrerPolicy && (a.referrerPolicy = r.referrerPolicy), r.crossOrigin === "use-credentials" ? a.credentials = "include" : r.crossOrigin === "anonymous" ? a.credentials = "omit" : a.credentials = "same-origin", a
    }

    function C(r) {
        if (r.ep) return;
        r.ep = !0;
        const a = i(r);
        fetch(r.href, a)
    }
})();
const x5 = {
        vi: {
            translation: {
                header: {
                    home: "ThÃ´ng tin chuyá»ƒn khoáº£n",
                    selectBank: "Chá»n ngÃ¢n hÃ ng cá»§a báº¡n",
                    searchBank: "TÃ¬m ngÃ¢n hÃ ng",
                    momo: "ThÃ´ng tin chuyá»ƒn khoáº£n",
                    feedback: "ÄÃ¡nh giÃ¡ vÃ  pháº£n há»“i"
                },
                button: {
                    saveToQRWallet: "LÆ°u vÃ o VÃ­ QR",
                    openBankingApp: "Má»Ÿ á»©ng dá»¥ng ngÃ¢n hÃ ng",
                    cancel: "Há»§y",
                    done: "Xong",
                    ok: "ÄÃ£ hiá»ƒu",
                    copy: "Sao chÃ©p",
                    viewAll: "Xem thÃªm",
                    openMomoApp: "Má»Ÿ MoMo",
                    finish: "HoÃ n thÃ nh",
                    continue: "Tiáº¿p tá»¥c",
                    gotIt: "ÄÃ£ hiá»ƒu"
                },
                label: {
                    fullName: "Há» vÃ  tÃªn",
                    phoneNumber: "Sá»‘ Ä‘iá»‡n thoáº¡i",
                    bank: "NgÃ¢n hÃ ng",
                    accountName: "Chá»§ tÃ i khoáº£n",
                    accountNumber: "Sá»‘ tÃ i khoáº£n",
                    cardNumber: "Sá»‘ tháº»",
                    amount: "Sá»‘ tiá»n (Ä‘)",
                    content: "Ná»™i dung chuyá»ƒn khoáº£n",
                    merchant: "Cá»­a hÃ ng",
                    store: "Äiá»ƒm bÃ¡n",
                    opening: "Äang má»Ÿ...",
                    openingMomoApp: "Äang má»Ÿ MoMo...",
                    openingApp: "Äang má»Ÿ á»©ng dá»¥ng ngÃ¢n hÃ ng...",
                    copyAndPasteToApp: "Sao chÃ©p vÃ  dÃ¡n vÃ o á»©ng dá»¥ng ngÃ¢n hÃ ng",
                    disclaimer: "Zalo chÆ°a há»— trá»£ tá»± Ä‘á»™ng dÃ¡n sá»‘ tÃ i khoáº£n vÃ o á»©ng dá»¥ng ngÃ¢n hÃ ng",
                    promoteAutofill: "Ä‘Ã£ há»— trá»£ tá»± Ä‘á»™ng Ä‘iá»n thÃ´ng tin chuyá»ƒn khoáº£n vÃ o á»©ng dá»¥ng ngÃ¢n hÃ ng",
                    bannerPromoteQRWallet: "Táº¡o mÃ£ QR chuyá»ƒn khoáº£n cá»§a riÃªng báº¡n",
                    enterYourFeedback: "Nháº­p pháº£n há»“i cá»§a báº¡n",
                    question: "CÃ¢u há»i",
                    autofill: "Tá»± Ä‘á»™ng Ä‘iá»n"
                },
                title: {
                    recent: "Gáº§n Ä‘Ã¢y",
                    popular: "Phá»• biáº¿n",
                    all: "Táº¥t cáº£",
                    alert: "ThÃ´ng bÃ¡o",
                    btmSheetSearch: "TÃ¬m ngÃ¢n hÃ ng cá»§a báº¡n"
                },
                input: {
                    searchYourBank: "TÃ¬m ngÃ¢n hÃ ng cá»§a báº¡n",
                    typeYourBank: "Nháº­p tÃªn ngÃ¢n hÃ ng"
                },
                message: {
                    copied: "ÄÃ£ sao chÃ©p",
                    copiedContent: "ÄÃ£ sao chÃ©p {{content}}",
                    contentInvalid: "MÃ£ QR khÃ´ng há»£p lá»‡",
                    cannotOpenBankingApp: "KhÃ´ng thá»ƒ má»Ÿ á»©ng dá»¥ng ngÃ¢n hÃ ng nÃ y",
                    pleaseInstallOrTryAgain: "Vui lÃ²ng cÃ i Ä‘áº·t hoáº·c thá»­ láº¡i vá»›i ngÃ¢n hÃ ng khÃ¡c",
                    noBankResults: "KhÃ´ng tÃ¬m tháº¥y ngÃ¢n hÃ ng",
                    closeAfterSeconds: "Quay láº¡i sau {{count}} giÃ¢y..."
                },
                home: {
                    "vietqr.step1.label": "1. Sao chÃ©p sá»‘ tÃ i khoáº£n",
                    "vietqr.step2.label": "2. DÃ¡n vÃ o á»©ng dá»¥ng ngÃ¢n hÃ ng cá»§a báº¡n",
                    "vnpay.step2.label": "Má»Ÿ nhanh á»©ng dá»¥ng ngÃ¢n hÃ ng cá»§a báº¡n"
                },
                feedback: {
                    bankCSC: {
                        q1: {
                            title: "Má»©c Ä‘á»™ hÃ i lÃ²ng cá»§a báº¡n vá»›i tÃ­nh nÄƒng tá»± Ä‘á»™ng hiá»ƒn thá»‹ tháº» thÃ´ng tin chuyá»ƒn khoáº£n trÃªn Zalo?",
                            opt1: "Ráº¥t khÃ´ng hÃ i lÃ²ng",
                            opt2: "KhÃ´ng hÃ i lÃ²ng",
                            opt3: "BÃ¬nh thÆ°á»ng",
                            opt4: "HÃ i lÃ²ng",
                            opt5: "Ráº¥t hÃ i lÃ²ng"
                        },
                        q2: {
                            title: "Vui lÃ²ng cho biáº¿t vÃ¬ sao báº¡n chá»n {{answer}}"
                        },
                        q3: {
                            title: "Báº¡n cÃ³ muá»‘n tiáº¿p tá»¥c sá»­ dá»¥ng tÃ­nh nÄƒng tá»± Ä‘á»™ng hiá»ƒn thá»‹ tháº» thÃ´ng tin chuyá»ƒn khoáº£n má»›i nÃ y?",
                            opt1: "CÃ³, tÃ´i muá»‘n sá»­ dá»¥ng tiáº¿p",
                            opt2: "KhÃ´ng, tÃ´i khÃ´ng muá»‘n sá»­ dá»¥ng ná»¯a"
                        },
                        thanks: "Cáº£m Æ¡n báº¡n Ä‘Ã£ dÃ nh thá»i gian lÃ m kháº£o sÃ¡t Ä‘á»ƒ giÃºp Zalo ngÃ y cÃ ng cáº£i thiá»‡n hÆ¡n."
                    }
                },
                disclaimer: {
                    check_info: "Báº¡n vui lÃ²ng kiá»ƒm tra ká»¹ thÃ´ng tin trÆ°á»›c khi thá»±c hiá»‡n báº¥t ká»³ thao tÃ¡c nÃ o. Zalo khÃ´ng chá»‹u trÃ¡ch nhiá»‡m vá» tÃ­nh xÃ¡c thá»±c thÃ´ng tin chuyá»ƒn khoáº£n."
                },
                autofill: {
                    bannerTitle: "Tá»° Äá»˜NG ÄIá»€N",
                    bannerDesc: "NgÃ¢n hÃ ng Ä‘Ã£ há»— trá»£ tá»± Ä‘á»™ng Ä‘iá»n thÃ´ng tin chuyá»ƒn khoáº£n.",
                    bannerCta: "TÃ¬m hiá»ƒu thÃªm",
                    btmSheetTitle: "TÃ¬m hiá»ƒu thÃªm",
                    btmShetDescLine1: 'Tháº» "Tá»° Äá»˜NG ÄIá»€N" dÃ nh cho nhá»¯ng ngÃ¢n hÃ ng Ä‘Ã£ há»— trá»£ tá»± Ä‘á»™ng Ä‘iá»n thÃ´ng tin ngÆ°á»i nháº­n khi báº¡n chá»n á»©ng dá»¥ng ngÃ¢n hÃ ng trong mÃ n hÃ¬nh ThÃ´ng tin chuyá»ƒn khoáº£n.',
                    btmShetDescLine2: "NgÃ¢n hÃ ng {{banks}} Ä‘Ã£ há»— trá»£ tá»± Ä‘á»™ng Ä‘iá»n."
                }
            }
        },
        en: {
            translation: {
                header: {
                    home: "Transfer details",
                    selectBank: "Select your bank",
                    searchBank: "Search bank",
                    momo: "Transfer details",
                    feedback: "Rate and feedback"
                },
                button: {
                    saveToQRWallet: "Save to QR Wallet",
                    openBankingApp: "Open banking app",
                    cancel: "Cancel",
                    done: "Done",
                    ok: "Ok",
                    copy: "Copy",
                    viewAll: "See more",
                    openMomoApp: "Open MoMo",
                    finish: "Finish",
                    continue: "Continue",
                    gotIt: "Got it"
                },
                label: {
                    fullName: "Fullname",
                    phoneNumber: "Phone number",
                    bank: "Bank",
                    accountName: "Account name",
                    accountNumber: "Account number",
                    cardNumber: "Card number",
                    amount: "Amount (Ä‘)",
                    content: "Description",
                    merchant: "Merchant",
                    store: "Store",
                    opening: "Opening...",
                    openingMomoApp: "Opening MoMo...",
                    openingApp: "Opening your banking app...",
                    copyAndPasteToApp: "Copy and paste to your banking app",
                    disclaimer: "Account number autofill is not supported yet",
                    promoteAutofill: "have supported autofill transfer details into banking app",
                    bannerPromoteQRWallet: "Create your own banking QR code",
                    enterYourFeedback: "Enter your feedback",
                    question: "Question",
                    autofill: "Autofill"
                },
                title: {
                    recent: "Recent",
                    popular: "Popular",
                    all: "All",
                    alert: "Alert",
                    btmSheetSearch: "Search your bank"
                },
                input: {
                    searchYourBank: "Search your bank",
                    typeYourBank: "Type bank name"
                },
                message: {
                    copied: "Copied",
                    copiedContent: "{{content}} copied",
                    contentInvalid: "QR code invalid",
                    cannotOpenBankingApp: "Unable to open this banking app",
                    pleaseInstallOrTryAgain: "Please install or try again with another bank",
                    noBankResults: "No results",
                    closeAfterSeconds_one: "Close after {{count}} second...",
                    closeAfterSeconds_other: "Close after {{count}} seconds..."
                },
                home: {
                    "vietqr.step1.label": "1. Copy account number",
                    "vietqr.step2.label": "2. Paste it into your banking app",
                    "vnpay.step2.label": "Open your banking app"
                },
                feedback: {
                    bankCSC: {
                        q1: {
                            title: "How satisfied are you with the automatic display of transfer information cards on Zalo?",
                            opt1: "Dissatisfied",
                            opt2: "Unsatisfied",
                            opt3: "Normal",
                            opt4: "Satisfied",
                            opt5: "Very satisfied"
                        },
                        q2: {
                            title: "Please tell us why you chose {{answer}}"
                        },
                        q3: {
                            title: "Would you like to continue using this new automatic card transfer feature?",
                            opt1: "Yes, I want to use it again",
                            opt2: "No, I don't want to use it anymore"
                        },
                        thanks: "Thank you for taking the time to do this survey to help Zalo improve more."
                    }
                },
                disclaimer: {
                    check_info: "Please check the information carefully before taking any action. Zalo is not responsible for the authenticity of transfer information."
                },
                autofill: {
                    bannerTitle: "AUTOFILL",
                    bannerDesc: "The banks have supported autofill transfer detail.",
                    bannerCta: "Learn more",
                    btmSheetTitle: "Learn more",
                    btmShetDescLine1: '"AUTOFILL" badge is for banks that support automatic recipient account information filling when you select a banking app on the Transfer detail screen.',
                    btmShetDescLine2: "{{banks}} have already supported autofill."
                }
            }
        }
    },
    S5 = () => {
        const e = navigator.userAgent,
            i = /ZaloLanguage\/(\w+)/gm.exec(e);
        return (i == null ? void 0 : i[1]) === "vn" ? "vi" : (i == null ? void 0 : i[1]) || "vi"
    },
    H5 = S5();
a5.use(r5).init({
    resources: x5,
    lng: H5,
    interpolation: {
        escapeValue: !1
    }
});
var q1;
const I5 = V.div(q1 || (q1 = k(["\n  border-radius: 16px;\n  box-shadow: ", ";\n  background-color: #fff;\n  transition: all 0.3s ease-in-out;\n"])), ({
        shadow: e
    }) => e ? "var(--zmp-shadow-btm-3)" : "none"),
    Q2 = ({
        onClick: e,
        top: n
    }) => t.jsx(y5, {
        top: n,
        onClick: e,
        children: t.jsx(n1, {
            icon: "zi-close"
        })
    });
var X1;
const y5 = V.div(X1 || (X1 = k(["\n  position: absolute;\n  box-sizing: border-box;\n  width: 24px;\n  height: 24px;\n  right: 16px;\n  top: ", "px;\n"])), e => {
    var n;
    return (n = e.top) != null ? n : 24
});
var Y1;
V.span(Y1 || (Y1 = k(["\n  background-color: var(--zmp-text-02);\n  width: 4px;\n  height: 4px;\n  margin: 2px;\n  border-radius: 100%;\n  display: inline-block;\n  animation: pulse 1s ", "s infinite cubic-bezier(0.2, 0.68, 0.18, 1.08);\n  animation-fill-mode: both;\n"])), e => e.delay * .2);
var J1;
const M5 = V.div(J1 || (J1 = k(["\n  box-sizing: border-box;\n  position: fixed;\n  bottom: 0;\n  width: 100vw;\n  padding: 16px;\n"])));
var e2;
V.div(e2 || (e2 = k(["\n  margin-top: auto;\n  padding: 16px 24px;\n"])));
var n2;
const r1 = V.div(n2 || (n2 = k(["\n  display: flex;\n  flex-direction: column;\n  box-sizing: border-box;\n  padding: 24px 16px 48px 16px;\n  min-height: 100vh;\n  background-color: ", ";\n"])), ({
    bgGray: e
}) => e ? "#F4F5F6" : "var(--zmp-color-bg)");
var t2;
V.div(t2 || (t2 = k(["\n  display: grid;\n  grid-template-columns: repeat(", ", 1fr);\n  gap: ", "px;\n  grid-gap: ", "px;\n"])), e => {
    var n;
    return (n = e.col) != null ? n : 1
}, e => {
    var n;
    return (n = e.gap) != null ? n : 0
}, e => {
    var n;
    return (n = e.gap) != null ? n : 0
});
const w1 = (e, n = 200) => {
        const [i, C] = p.useState(!0), [r, a] = u1(() => ({
            opacity: e ? 1 : 0,
            scale: e ? 1 : 0,
            from: {
                opacity: 0,
                scale: 0
            },
            config: {
                duration: n
            },
            onResolve: () => {
                e || C(!0)
            }
        }), [e]);
        return p.useEffect(() => {
            e && C(!1)
        }, [e]), {
            props: r,
            api: a,
            unmounted: i
        }
    },
    v5 = ({
        size: e = 24
    }) => t.jsxs("svg", {
        width: e,
        height: e,
        viewBox: "0 0 56 56",
        fill: "none",
        xmlns: "http://www.w3.org/2000/svg",
        children: [t.jsxs("g", {
            clipPath: "url(#clip0_2582_119204)",
            children: [t.jsx("path", {
                d: "M28 53.8311C42.2662 53.8311 53.8311 42.2662 53.8311 28C53.8311 13.7339 42.2662 2.16895 28 2.16895C13.7339 2.16895 2.16895 13.7339 2.16895 28C2.16895 42.2662 13.7339 53.8311 28 53.8311Z",
                fill: "#34B764"
            }), t.jsx("path", {
                d: "M28 56C12.562 56 0 43.4401 0 28C0 12.562 12.562 0 28 0C43.4401 0 56 12.562 56 28C56 43.4401 43.4401 56 28 56ZM28 4.3377C14.9521 4.3377 4.3377 14.9521 4.3377 28C4.3377 41.0479 14.9521 51.6623 28 51.6623C41.0479 51.6623 51.6623 41.0457 51.6623 28C51.6623 14.9521 41.0479 4.3377 28 4.3377Z",
                fill: "#34B764"
            }), t.jsx("path", {
                d: "M24.6166 38.3021C24.3287 38.3022 24.0436 38.2449 23.7781 38.1336C23.5126 38.0222 23.2719 37.8591 23.0702 37.6536L15.0671 29.5204C14.2277 28.6659 14.2386 27.2952 15.0931 26.4536C15.9477 25.6165 17.3205 25.6251 18.1599 26.4797L24.5537 32.9775L37.7817 18.4093C38.5906 17.5223 39.9614 17.4594 40.844 18.2619C41.7311 19.0666 41.7962 20.4372 40.9915 21.3265L26.2216 37.5928C26.0234 37.8114 25.7826 37.9872 25.5142 38.1095C25.2457 38.2318 24.955 38.2981 24.66 38.3042C24.6448 38.3021 24.6318 38.3021 24.6166 38.3021Z",
                fill: "white"
            })]
        }), t.jsx("defs", {
            children: t.jsx("clipPath", {
                id: "clip0_2582_119204",
                children: t.jsx("rect", {
                    width: "56",
                    height: "56",
                    fill: "white"
                })
            })
        })]
    }),
    _5 = e => {
        const {
            size: n = 24
        } = e;
        return t.jsxs("svg", {
            width: n,
            height: n,
            viewBox: "0 0 40 40",
            fill: "none",
            xmlns: "http://www.w3.org/2000/svg",
            children: [t.jsx("rect", {
                x: "0.25",
                y: "0.25",
                width: "39.5",
                height: "39.5",
                rx: "7.75",
                fill: "#A50064"
            }), t.jsx("path", {
                d: "M28.3251 6.79982C24.9045 6.79982 22.1319 9.46686 22.1319 12.7536C22.1319 16.0402 24.9118 18.7073 28.3251 18.7073C31.7385 18.7073 34.5256 16.0402 34.5256 12.7536C34.5256 9.46686 31.753 6.79982 28.3251 6.79982ZM28.3251 15.2938C27.6403 15.3064 26.9784 15.0463 26.485 14.5707C25.9916 14.095 25.707 13.4428 25.6936 12.7572C25.729 12.0824 26.0217 11.4469 26.5113 10.9818C27.0009 10.5166 27.6502 10.2574 28.3251 10.2574C29.0001 10.2574 29.6494 10.5166 30.139 10.9818C30.6286 11.4469 30.9213 12.0824 30.9566 12.7572C30.9433 13.4428 30.6587 14.095 30.1653 14.5707C29.6718 15.0463 29.01 15.3064 28.3251 15.2938ZM20.3619 11.2715V18.7326H16.7856V11.2352C16.7856 10.9565 16.675 10.6892 16.4782 10.4921C16.2813 10.2951 16.0143 10.1844 15.7359 10.1844C15.4575 10.1844 15.1905 10.2951 14.9937 10.4921C14.7968 10.6892 14.6862 10.9565 14.6862 11.2352V18.7326H11.1244V11.2352C11.1244 10.9565 11.0138 10.6892 10.817 10.4921C10.6201 10.2951 10.3531 10.1844 10.0747 10.1844C9.79633 10.1844 9.52933 10.2951 9.33248 10.4921C9.13562 10.6892 9.02502 10.9565 9.02502 11.2352V18.7326H5.47412V11.2715C5.50073 10.0617 6.00519 8.91182 6.877 8.07368C7.74882 7.23554 8.9169 6.77748 10.1254 6.79982C11.1259 6.79777 12.1014 7.1123 12.9126 7.6985C13.7231 7.1137 14.697 6.79927 15.6961 6.79982C16.9068 6.77455 18.0781 7.23121 18.9528 8.06956C19.8276 8.90791 20.3343 10.0595 20.3619 11.2715ZM28.3251 21.2692C24.9045 21.2692 22.1319 23.9326 22.1319 27.223C22.1319 30.5133 24.9118 33.1876 28.3251 33.1876C31.7385 33.1876 34.5184 30.5241 34.5184 27.2375C34.5184 23.9508 31.753 21.2692 28.3251 21.2692ZM28.3251 29.7632C27.8286 29.744 27.3487 29.5791 26.9451 29.2889C26.5414 28.9988 26.2319 28.5963 26.0551 28.1314C25.8782 27.6666 25.8417 27.1599 25.9503 26.6745C26.0588 26.189 26.3075 25.7463 26.6654 25.4012C27.0234 25.0562 27.4748 24.8242 27.9634 24.7339C28.4521 24.6437 28.9564 24.6994 29.4137 24.8939C29.8711 25.0884 30.2612 25.4133 30.5355 25.828C30.8098 26.2428 30.9563 26.7291 30.9566 27.2266C30.9519 27.5673 30.88 27.9037 30.7451 28.2165C30.6102 28.5294 30.4148 28.8124 30.1703 29.0495C29.9258 29.2865 29.6369 29.4729 29.3203 29.5978C29.0036 29.7228 28.6655 29.7839 28.3251 29.7777V29.7632ZM20.3619 25.7554V33.2021H16.7856V25.7155C16.7856 25.4368 16.675 25.1695 16.4782 24.9724C16.2813 24.7754 16.0143 24.6646 15.7359 24.6646C15.4575 24.6646 15.1905 24.7754 14.9937 24.9724C14.7968 25.1695 14.6862 25.4368 14.6862 25.7155V33.2021H11.1244V25.7155C11.1244 25.4368 11.0138 25.1695 10.817 24.9724C10.6201 24.7754 10.3531 24.6646 10.0747 24.6646C9.79633 24.6646 9.52933 24.7754 9.33248 24.9724C9.13562 25.1695 9.02502 25.4368 9.02502 25.7155V33.2021H5.47412V25.7554C5.48495 25.155 5.61389 24.5626 5.85357 24.0121C6.09324 23.4616 6.43896 22.9638 6.87094 22.5471C7.30292 22.1305 7.8127 21.8032 8.37112 21.5839C8.92955 21.3646 9.52567 21.2577 10.1254 21.2692C11.1252 21.2676 12.1003 21.5807 12.9126 22.1643C13.7232 21.5801 14.6973 21.2669 15.6961 21.2692C16.2969 21.2563 16.8944 21.3621 17.4543 21.5807C18.0141 21.7992 18.5255 22.1263 18.9589 22.543C19.3923 22.9598 19.7393 23.458 19.9801 24.0092C20.2208 24.5605 20.3506 25.1539 20.3619 25.7554Z",
                fill: "white"
            }), t.jsx("rect", {
                x: "0.25",
                y: "0.25",
                width: "39.5",
                height: "39.5",
                rx: "7.75",
                stroke: "#D6D9DC",
                strokeWidth: "0.5"
            })]
        })
    },
    K5 = ({
        size: e = 32,
        spin: n
    }) => {
        const i = p.useMemo(() => n ? "spin" : "", [n]);
        return t.jsxs("svg", {
            width: e,
            height: e,
            viewBox: "0 0 33 32",
            fill: "none",
            xmlns: "http://www.w3.org/2000/svg",
            className: i,
            children: [t.jsx("path", {
                d: "M32.5 16C32.5 24.8366 25.3366 32 16.5 32C7.66344 32 0.5 24.8366 0.5 16C0.5 7.16344 7.66344 0 16.5 0C25.3366 0 32.5 7.16344 32.5 16ZM3.5 16C3.5 23.1797 9.3203 29 16.5 29C23.6797 29 29.5 23.1797 29.5 16C29.5 8.8203 23.6797 3 16.5 3C9.3203 3 3.5 8.8203 3.5 16Z",
                fill: "black",
                fillOpacity: "0.1"
            }), t.jsx("path", {
                d: "M21.4593 2.37446C21.7426 1.59599 22.6073 1.18826 23.3558 1.54323C24.7965 2.22647 26.1297 3.1225 27.3094 4.20356C28.8586 5.62308 30.1129 7.33382 31.0009 9.23811C31.8889 11.1424 32.3931 13.2029 32.4848 15.3021C32.5546 16.9007 32.384 18.4979 31.9813 20.0408C31.7721 20.8424 30.904 21.2426 30.1255 20.9593C29.3471 20.676 28.9548 19.8162 29.1467 19.0103C29.4248 17.8417 29.5402 16.6378 29.4876 15.433C29.4132 13.7274 29.0035 12.0532 28.282 10.506C27.5605 8.95873 26.5413 7.56875 25.2827 6.4154C24.3935 5.60061 23.3971 4.91519 22.3231 4.37712C21.5825 4.00604 21.176 3.15292 21.4593 2.37446Z",
                fill: "#52A0FF"
            })]
        })
    },
    w5 = e => {
        const {
            size: n = 24
        } = e;
        return t.jsxs("svg", {
            width: n,
            height: n,
            viewBox: "0 0 34 8",
            fill: "none",
            xmlns: "http://www.w3.org/2000/svg",
            children: [t.jsx("path", {
                d: "M23.8926 4.30175H22.2134L23.0305 1.98011L23.8926 4.30175ZM15.4795 0.289591L17.0686 0.283956H19.0014C20.0608 0.283956 20.9342 1.15175 20.9342 2.21678V2.45345C20.9342 3.51848 20.0664 4.32429 19.0014 4.3581L18.1223 4.38628C18.8324 4.05945 19.1254 3.23673 19.0352 2.49853C18.962 1.90122 18.6577 1.33208 18.1505 1.32081L17.8293 1.31517V6.60649C17.8293 6.70792 17.8462 6.753 17.9026 6.84316C17.9871 6.98968 18.1054 7.13055 18.2238 7.27706C18.2519 7.31651 18.2858 7.35032 18.3196 7.38977H15.5809C15.6204 7.33905 15.6598 7.28833 15.6993 7.23762C15.7838 7.12492 15.857 7.00658 15.9134 6.87134C15.9472 6.78681 15.9641 6.71919 15.9641 6.62903V0.937622C15.9472 0.638964 15.6542 0.469913 15.4795 0.289591ZM28.6317 4.08199L26.1467 0.514993L25.8931 0.283956H28.3443L30.0067 2.97751L30.1419 2.87045L31.145 1.37716C31.3929 1.01088 31.3591 0.582614 31.0097 0.283956H33.3257L30.6491 4.08199V6.83753L31.1224 7.40104H28.2429L28.6486 6.8488C28.643 5.92465 28.6092 4.99486 28.6317 4.08199ZM21.8809 0.283956C22.0781 0.554438 22.1401 0.650234 22.1627 0.892542C22.1796 1.06159 22.1683 1.15739 22.112 1.31517L20.2637 6.67975C20.1791 6.89952 19.9988 7.14182 19.7396 7.3785H21.7569C21.6048 7.24325 21.509 7.08547 21.4752 6.89952C21.4414 6.72483 21.447 6.66284 21.4808 6.49943L21.8922 5.2259H24.242L24.6083 6.2064C24.6477 6.30783 24.6703 6.40363 24.6759 6.51633C24.7097 6.88261 24.5914 7.1869 24.2984 7.3954H27.4596C27.1497 7.11928 26.8623 6.83189 26.7045 6.47689L24.3942 0.27832H21.8809V0.283956Z",
                fill: "#005BA8"
            }), t.jsx("path", {
                d: "M0.636719 0.25H2.84566L4.6996 5.5695L6.27178 1.16288C6.29995 0.993828 6.27741 0.937477 6.20979 0.790966C6.12527 0.610644 6.02947 0.441592 5.94494 0.26127H7.59602C7.50022 0.621914 7.35371 1.01637 7.22974 1.37701L5.09969 7.57558C4.51927 7.45724 3.87124 7.23184 3.36972 6.75286C2.99217 6.39785 2.85693 5.98649 2.67098 5.50188L0.890297 0.779696C0.811406 0.593739 0.72688 0.424687 0.636719 0.25ZM9.46122 2.74633V6.55C9.46122 6.70214 9.49503 6.73032 9.59083 6.85429L10.0247 7.42343H7.94539C8.06373 7.24311 8.18206 7.06842 8.29476 6.8881C8.38492 6.74159 8.42437 6.69087 8.42437 6.52182V1.21359L7.83832 0.26127H9.99655L13.4847 4.75805V1.17415C13.4847 1.0051 13.4508 0.948748 13.3607 0.802236C13.2424 0.621914 13.1184 0.452862 13.0057 0.27254H15.085L14.6511 0.841681C14.5553 0.965653 14.5215 0.993828 14.5215 1.14597V7.61502C13.7326 7.51359 13 7.31636 12.3464 6.48801L9.46122 2.74633Z",
                fill: "#EB2027"
            })]
        })
    },
    R5 = e => {
        const {
            size: n = 24
        } = e;
        return t.jsxs("svg", {
            width: n,
            height: n,
            viewBox: "0 0 40 40",
            fill: "none",
            xmlns: "http://www.w3.org/2000/svg",
            children: [t.jsx("rect", {
                x: "0.25",
                y: "0.25",
                width: "39.5",
                height: "39.5",
                rx: "7.75",
                fill: "white"
            }), t.jsx("path", {
                d: "M22.2885 10.4116C22.0741 10.1903 21.7976 10.0797 21.4657 10.0797C20.9748 10.0797 20.6222 10.3148 20.394 10.7849C19.917 10.2249 19.2602 9.94141 18.4305 9.94141C17.4349 9.94141 16.5983 10.3286 15.9138 11.096C15.2362 11.8635 14.8975 12.8038 14.8975 13.91C14.8975 15.0162 15.2362 15.9565 15.9138 16.724C16.5914 17.4914 17.4349 17.8786 18.4305 17.8786C19.2602 17.8786 19.917 17.5951 20.394 17.0351C20.6153 17.5053 20.9748 17.7403 21.4657 17.7403C21.7976 17.7403 22.0741 17.6297 22.2885 17.4085C22.5028 17.1872 22.6134 16.9176 22.6134 16.5995V11.2274C22.6065 10.9024 22.5028 10.6328 22.2885 10.4116ZM19.9032 15.2375C19.6266 15.597 19.2394 15.7768 18.7554 15.7768C18.2646 15.7768 17.8843 15.597 17.6077 15.2375C17.3312 14.878 17.1929 14.4355 17.1929 13.9031C17.1929 13.3707 17.3312 12.9282 17.6077 12.5687C17.8843 12.2092 18.2715 12.0294 18.7554 12.0294C19.2463 12.0294 19.6266 12.2092 19.9032 12.5687C20.1797 12.9282 20.318 13.3707 20.318 13.9031C20.3249 14.4355 20.1866 14.878 19.9032 15.2375Z",
                fill: "#118ACB"
            }), t.jsx("path", {
                d: "M25.1992 17.401C24.9849 17.6223 24.7083 17.7329 24.3765 17.7329C24.0446 17.7329 23.768 17.6223 23.5537 17.401C23.3394 17.1798 23.2288 16.9101 23.2288 16.5921V6.97478C23.2288 6.65674 23.3394 6.3871 23.5537 6.16585C23.768 5.94461 24.0446 5.83398 24.3765 5.83398C24.7083 5.83398 24.9849 5.94461 25.1992 6.16585C25.4136 6.3871 25.5242 6.65674 25.5242 6.97478V16.5921C25.5242 16.9101 25.4136 17.1798 25.1992 17.401Z",
                fill: "#118ACB"
            }), t.jsx("path", {
                d: "M32.777 11.096C32.0441 10.3286 31.1108 9.94141 29.9769 9.94141C28.843 9.94141 27.9165 10.3217 27.1975 11.0822C26.4784 11.8427 26.1189 12.783 26.1189 13.91C26.1189 15.037 26.4784 15.9773 27.1975 16.7378C27.9165 17.4983 28.843 17.8786 29.9769 17.8786C31.1108 17.8786 32.0441 17.4914 32.777 16.724C33.4822 15.9704 33.8349 15.037 33.8349 13.91C33.8279 12.783 33.4753 11.8427 32.777 11.096ZM31.1246 15.2375C30.848 15.597 30.4609 15.7768 29.9769 15.7768C29.486 15.7768 29.1057 15.597 28.8292 15.2375C28.5526 14.878 28.4143 14.4355 28.4143 13.9031C28.4143 13.3707 28.5526 12.9282 28.8292 12.5687C29.1057 12.2092 29.4929 12.0294 29.9769 12.0294C30.4678 12.0294 30.848 12.2092 31.1246 12.5687C31.4011 12.9282 31.5394 13.3707 31.5394 13.9031C31.5394 14.4355 31.4011 14.878 31.1246 15.2375Z",
                fill: "#118ACB"
            }), t.jsx("path", {
                d: "M13.6323 10.2039C14.4412 9.15992 14.8422 8.46161 14.8422 8.09517C14.8422 7.25859 14.3167 6.84375 13.2658 6.84375H7.71393C7.27835 6.84375 6.93957 6.94746 6.70449 7.15488C6.4625 7.3623 6.34497 7.63194 6.34497 7.9569C6.34497 8.28876 6.4625 8.55149 6.70449 8.75891C6.94648 8.96633 7.27835 9.07004 7.71393 9.07004H11.5235L6.64918 15.3756C6.33114 15.7904 6.17212 16.1568 6.17212 16.4749C6.17212 17.3944 6.78055 17.8507 7.99048 17.8507H13.7152C14.6279 17.8507 15.0842 17.4636 15.0842 16.6961C15.0842 15.9287 14.6279 15.5415 13.7152 15.5415H9.50464L13.6323 10.2039Z",
                fill: "#118ACB"
            }), t.jsx("path", {
                d: "M10.9013 23.7891H9.47705V26.7482H10.9013C11.33 26.7482 11.6757 26.61 11.9453 26.3265C12.2081 26.0499 12.3463 25.6904 12.3463 25.2617C12.3463 24.8331 12.215 24.4805 11.9453 24.197C11.6757 23.9273 11.33 23.7891 10.9013 23.7891Z",
                fill: "#33B44A"
            }), t.jsx("path", {
                d: "M18.0159 26.5762C17.5665 26.5762 17.207 26.7421 16.9511 27.074C16.6953 27.4058 16.564 27.8207 16.564 28.3047C16.564 28.7955 16.6953 29.2035 16.9511 29.5353C17.207 29.8672 17.5665 30.0331 18.0159 30.0331C18.4653 30.0331 18.8248 29.8672 19.0806 29.5353C19.3365 29.2035 19.4678 28.7886 19.4678 28.3047C19.4678 27.8138 19.3365 27.4058 19.0806 27.074C18.8179 26.7421 18.4653 26.5762 18.0159 26.5762Z",
                fill: "#33B44A"
            }), t.jsx("path", {
                d: "M28.0825 19.5586H7.41671C6.72531 19.5586 6.16528 20.1186 6.16528 20.81V32.9163C6.16528 33.6077 6.72531 34.1678 7.41671 34.1678H23.7267C23.5538 34.0018 23.4709 33.8151 23.4709 33.5939C23.4709 33.4141 23.5124 33.2275 23.5884 33.0339L24.3559 31.3261L22.2333 26.0024C22.1711 25.8503 22.1365 25.6843 22.1365 25.5046C22.1365 25.2695 22.2333 25.0759 22.4338 24.9169C22.6274 24.7579 22.8348 24.6749 23.0491 24.6749C23.5193 24.6749 23.8442 24.9031 24.0102 25.3594L25.3376 28.9823L26.755 25.3594C26.9348 24.9031 27.2528 24.6749 27.716 24.6749C27.9304 24.6749 28.1378 24.7579 28.3314 24.9169C28.525 25.0759 28.6287 25.2764 28.6287 25.5046C28.6287 25.6843 28.5941 25.8503 28.5319 26.0024L25.386 33.6561C25.3031 33.8705 25.1925 34.0364 25.0749 34.1608H28.0825C28.7739 34.1608 29.3339 33.6008 29.3339 32.9094V20.8031C29.3339 20.1117 28.7739 19.5586 28.0825 19.5586ZM13.4871 27.7032C12.8372 28.2978 12.0145 28.5951 11.0258 28.5951H9.47706V30.8836C9.47706 31.2293 9.38027 31.499 9.18668 31.6856C8.99309 31.8792 8.73727 31.9691 8.43306 31.9691C8.12884 31.9691 7.87303 31.8723 7.67944 31.6856C7.48585 31.4921 7.38905 31.2293 7.38905 30.8836V23.0363C7.38905 22.3103 7.75549 21.9439 8.48145 21.9439H10.9566C11.9937 21.9439 12.8442 22.255 13.5217 22.8704C14.1993 23.4926 14.5381 24.2946 14.5381 25.2833C14.5242 26.2789 14.1785 27.0879 13.4871 27.7032ZM21.5834 30.7937C21.5834 31.091 21.4866 31.34 21.2861 31.5405C21.0856 31.7479 20.8367 31.8447 20.5255 31.8447C20.0761 31.8447 19.7443 31.6303 19.5368 31.1948C19.0944 31.7133 18.4859 31.976 17.7185 31.976C16.7989 31.976 16.0177 31.6234 15.3885 30.9113C14.7593 30.1992 14.4482 29.328 14.4482 28.3047C14.4482 27.2815 14.7593 26.4103 15.3885 25.6982C16.0177 24.986 16.792 24.6334 17.7185 24.6334C18.4859 24.6334 19.0944 24.8962 19.5368 25.4147C19.7443 24.9791 20.0761 24.7648 20.5255 24.7648C20.8298 24.7648 21.0856 24.8685 21.2861 25.069C21.4866 25.2764 21.5834 25.5253 21.5834 25.8157V30.7937Z",
                fill: "#39B54A"
            })]
        })
    },
    f1 = ({
        visible: e,
        text: n
    }) => {
        const {
            unmounted: i,
            props: {
                opacity: C,
                scale: r
            }
        } = w1(e);
        return i ? null : t.jsxs(O5, {
            children: [t.jsx(T5, {
                style: {
                    opacity: C
                }
            }), t.jsxs(j5, {
                style: {
                    scale: r,
                    opacity: C
                },
                children: [t.jsx(u, {
                    children: t.jsx(K5, {
                        spin: !0
                    })
                }), n && t.jsx(u, {
                    mt: 3,
                    children: t.jsx(L, {
                        children: n
                    })
                })]
            })]
        })
    };
var o2;
const O5 = V(Z.div)(o2 || (o2 = k(["\n  position: fixed;\n  z-index: 999999;\n  left: 0;\n  right: 0;\n  bottom: 0;\n  top: 0;\n  display: flex;\n  justify-content: center;\n  align-items: center;\n"])));
var i2;
const T5 = V(Z.div)(i2 || (i2 = k(["\n  position: absolute;\n  background: rgba(255, 255, 255, 0.7);\n  left: 0;\n  right: 0;\n  bottom: 0;\n  top: 0;\n"])));
var s2;
const j5 = V(Z.div)(s2 || (s2 = k(["\n  position: relative;\n  background: #ffffff;\n  box-shadow: 0px 10px 24px rgba(20, 20, 21, 0.09);\n  border-radius: 12px;\n  max-width: 224px;\n  padding: 24px;\n  box-sizing: border-box;\n  text-align: center;\n"]))),
    E2 = e => t.jsx(Q5, {
        ...e,
        children: t.jsx(P5, {})
    });
var C2;
const P5 = V.div(C2 || (C2 = k(["\n  box-sizing: border-box;\n  width: 48px;\n  height: 6px;\n  border-radius: 6px;\n  margin-top: 8px;\n  margin-bottom: 12px;\n  background-color: var(--zmp-color-ng20);\n"])));
var a2;
const Q5 = V.div(a2 || (a2 = k(["\n  display: flex;\n  justify-content: center;\n  box-sizing: border-box;\n  height: 24px;\n"])));
var r2;
const $ = V(L)(r2 || (r2 = k(["\n  text-align: ", ";\n  color: ", ";\n"])), ({
    align: e
}) => e || "left", ({
    color: e
}) => e && "var(--zmp-color-".concat(e, ")"));
var c2;
const o1 = V(L.Title)(c2 || (c2 = k(["\n  text-align: ", ";\n  color: ", ";\n"])), ({
    align: e
}) => e || "left", ({
    color: e
}) => e && "var(--zmp-color-".concat(e, ")"));
var l2;
V(Z.div)(l2 || (l2 = k(["\n  position: absolute;\n  top: 28px;\n  left: ", ";\n  right: ", ";\n  z-index: 2001;\n  max-width: calc(80vw);\n  /* transition: all 0.1s ease-in-out; */\n"])), e => e.align === "left" ? "0" : "auto", e => e.align === "right" ? "0" : "auto");
var p2;
V.div(p2 || (p2 = k(["\n  background-color: #006af5;\n  border-radius: 12px;\n  padding: 16px;\n  font-size: 14px;\n  line-height: 18px;\n  color: #fff;\n  margin-bottom: 12px;\n  text-align: left;\n  box-sizing: border-box;\n  /* transition: all 0.25s ease-in-out; */\n"])));
var u2;
V(Z.div)(u2 || (u2 = k(["\n  position: absolute;\n  left: 16px;\n  right: 16px;\n  top: ", "px;\n"])), e => {
    var n;
    return (n = e.top) != null ? n : 0
});
var d2;
V(Z.div)(d2 || (d2 = k(["\n  position: absolute;\n  display: flex;\n  justify-content: center;\n  justify-content: center;\n  z-index: 2001;\n  top: ", "px;\n  left: ", ";\n  transform: rotate(", "deg);\n  /* transition: all 0.1s ease-in-out; */\n"])), e => {
    var n;
    return ((n = e.top) != null ? n : 0) + 20
}, e => {
    var n, i;
    return (i = "".concat(((n = e.left) != null ? n : 0) - 4, "px")) != null ? i : "auto"
}, e => {
    var n;
    return (n = e.rotate) != null ? n : 0
});
const S1 = ({
        children: e
    }) => {
        const n = u1({
            from: {
                opacity: 0
            },
            to: {
                opacity: 1
            }
        });
        return t.jsx(Z.div, {
            style: n,
            children: e
        })
    },
    E5 = ({
        children: e
    }) => {
        const n = u1({
            from: {
                opacity: 0,
                transform: "scale(0.8)"
            },
            to: {
                opacity: 1,
                transform: "scale(1)"
            },
            config: {
                tension: 180,
                friction: 12,
                mass: 1,
                precision: .01,
                velocity: 0
            }
        });
        return t.jsx(Z.div, {
            style: n,
            children: e
        })
    },
    $1 = "zqrbanking_content",
    A1 = "zqrbanking_recentOpen",
    L5 = "zqrbanking_score",
    i1 = {
        setItem(e, n) {
            let i = n;
            typeof n == "object" && (i = JSON.stringify(n)), localStorage.setItem(e, i)
        },
        getItem(e) {
            const n = localStorage.getItem(e);
            return n && n.startsWith("{") ? JSON.parse(n) : n
        },
        removeItem(e) {
            localStorage.removeItem(e)
        }
    };

function Z5(e, n) {
    const i = {
        ...e
    };
    return n.forEach(C => delete i[C]), i
}
const R1 = c5(l5(e => ({
        openVietQRTipCount: 0,
        bannerAutofillClosed: !1,
        actions: {
            increaseOpenVietQRTipCount: n => {
                e(i => ({
                    openVietQRTipCount: i.openVietQRTipCount + n
                }))
            },
            closeBannerAutofill: (n = !0) => {
                e({
                    bannerAutofillClosed: n
                })
            }
        }
    }), {
        name: L5,
        partialize: e => Z5(e, ["actions"]),
        storage: i1
    })),
    L2 = () => _1(R1, e => e.actions),
    D5 = () => _1(R1, e => e.openVietQRTipCount),
    Z2 = () => _1(R1, e => e.bannerAutofillClosed),
    z5 = () => {
        const e = d1(),
            n = D5(),
            i = Z2(),
            C = L2(),
            r = i1.getItem(A1),
            a = p.useCallback(() => {
                i1.removeItem(A1), e.openSnackbar({
                    text: "ÄÃ£ xÃ³a! Vui lÃ²ng táº£i láº¡i trang"
                })
            }, [e]);
        return t.jsx(X, {
            children: t.jsx(r1, {
                children: t.jsx(U5, {
                    children: t.jsxs(e1, {
                        children: [t.jsx(e1.Item, {
                            title: "Recent apps",
                            subTitle: r || "Trá»‘ng",
                            suffix: t.jsx(U, {
                                size: "small",
                                variant: "secondary",
                                onClick: a,
                                children: "XÃ³a"
                            })
                        }), t.jsx(e1.Item, {
                            title: "Sá»‘ láº§n Má»Ÿ tooltip VietQR",
                            subTitle: "".concat(n, " láº§n"),
                            suffix: t.jsx(U, {
                                size: "small",
                                variant: "secondary",
                                onClick: () => C.increaseOpenVietQRTipCount(-1 * n),
                                children: "XÃ³a"
                            })
                        }), t.jsx(e1.Item, {
                            title: "Hiá»ƒn thá»‹ Banner Autofill",
                            subTitle: i ? "ÄÃ³ng" : "Má»Ÿ",
                            suffix: t.jsx(U, {
                                size: "small",
                                variant: "secondary",
                                onClick: () => C.closeBannerAutofill(!i),
                                children: i ? "Má»Ÿ" : "ÄÃ³ng"
                            })
                        })]
                    })
                })
            })
        })
    };
var h2;
const U5 = V.div(h2 || (h2 = k(["\n  border-radius: 12px;\n  border: 1px solid var(--zmp-border-01);\n  box-shadow: var(--zmp-shadow-01);\n  overflow: hidden;\n  overflow-wrap: anywhere;\n  word-break: break-word;\n"])));
var m2;
const H1 = V.div(m2 || (m2 = k(["\n  display: flex;\n  align-items: center;\n  padding: 16px;\n  border-radius: 8px;\n  border: 1px solid var(--zmp-color-border-01);\n  font-size: 16px;\n  line-height: 22px;\n  &:not(:last-child) {\n    margin-bottom: 16px;\n  }\n  &:active {\n    background-color: var(--zmp-pressed-bg-color);\n  }\n"]))),
    h1 = e => {
        p.useLayoutEffect(() => {
            window.document && e.trim().length > 0 && (window.document.title = e.trim())
        }, [e])
    },
    $5 = () => {
        const {
            userAgent: e
        } = window.navigator, n = /(Macintosh)|(MacIntel)|(MacPPC)|(Mac68K)/i, i = /(Win32)|(Win64)|(Windows)|(WinCE)/i, C = /(iPhone)|(iPad)|(iPod)/i;
        return n.test(e) ? "macos" : C.test(e) ? "ios" : i.test(e) ? "windows" : /Android/i.test(e) ? "android" : /Linux/i.test(e) ? "linux" : "undetermined"
    },
    Y = () => $5() === "ios",
    O = console,
    T = {
        closeWebview: () => {
            var e, n, i;
            (i = (n = (e = window.ZJSBridge) == null ? void 0 : e.H5) == null ? void 0 : n.closeWebview) == null || i.call(n)
        },
        hideKeyboard: () => {
            var e, n, i;
            (i = (n = (e = window.ZJSBridge) == null ? void 0 : e.Device) == null ? void 0 : n.hideKeyboard) == null || i.call(n)
        },
        openApp: (e, n) => {
            if (window.ZJSBridge && window.location.host.endsWith(".zalo.me")) O.log("openApp by ZJSBridge", e), window.ZJSBridge.Device.openApp(e, n);
            else {
                O.log("openApp by window.location", e);
                const i = Y() ? e.ios.url : e.android.url;
                window.location.href = i, n({
                    error_code: 0,
                    data: {}
                })
            }
        },
        openOutApp: (e, n) => {
            window.ZJSBridge && window.location.host.endsWith(".zalo.me") ? (O.log("openOutApp by ZJSBridge", e), window.ZJSBridge.Zalo.openOutApp(e, n)) : (O.log("openOutApp by window.location", e), window.location.href = e, n({
                error_code: 0,
                data: {}
            }))
        },
        openInApp: (e, n) => {
            window.ZJSBridge && window.location.host.endsWith(".zalo.me") ? (O.log("openInApp by ZJSBridge", e), window.ZJSBridge.Zalo.openInApp(e, n)) : (O.log("openInApp by window.location", e), window.location.href = e, n({
                error_code: 0,
                data: {}
            }))
        },
        openMiniApp: (e, n) => {
            if (window.ZJSBridge) window.ZJSBridge.Zalo.openMiniApp(e, n);
            else {
                const i = new URLSearchParams;
                Object.entries(e.params).forEach(([r, a]) => {
                    i.append(r, a)
                });
                const C = "https://zalo.me/s/".concat(e.appId, "/?").concat(i);
                window.location.href = C, n({
                    error_code: 0,
                    data: {}
                })
            }
        },
        openQR: e => {
            if (window.ZJSBridge && window.location.host.endsWith(".zalo.me")) window.ZJSBridge.callCustomAction("action.open.qr", {
                skipOpenLink: !0
            }, e);
            else {
                const n = window == null ? void 0 : window.prompt("Enter QR code");
                e({
                    error_code: 0,
                    data: {
                        content: n
                    }
                })
            }
        }
    };
window.location.search.includes("zdebug=true");
const O1 = "",
    G5 = e => {
        if (!e) return "";
        if (typeof e != "object") return e;
        const n = Object.keys(e),
            i = [];
        return n.forEach(C => {
            let r = e[C];
            typeof r == "object" ? r = JSON.stringify(r) : r = encodeURIComponent(r);
            const a = [C, r].join("=");
            i.push(a)
        }), i.join("&")
    },
    v = {
        PAGE_LOAD_DONE: "zqrbanking.pageload.done",
        CLICK_BUTTON_SAVE_TO_QRWALLET: "zqrbanking.click.btn.save.qrwallet",
        CLICK_BUTTON_OPEN_BANKING_APP: "zqrbanking.click.btn.open.banking.app",
        CLICK_BUTTON_DONE: "zqrbanking.click.btn.done",
        CLICK_BUTTON_COPY: "zqrbanking.click.btn.copy",
        CLICK_INPUT_SEARCH: "zqrbanking.click.inp.search",
        CLICK_ITEM_BANKING_APP: "zqrbanking.click.item.banking.app",
        OPEN_BANKING_APP_SUCCESS: "zqrbanking.open.banking.app.success",
        CLICK_BANNER_QRWALLET: "zqrbanking.click.banner.qrwallet",
        CLICK_DISCLAIMER: "zqrbanking.click.disclaimer",
        CLICK_BUTTON_VIEW_ALL: "zqrbanking.click.btn.view.all",
        LOOKUP_BANK_ACC_NAME_SUCCESS: "zqrbanking.lookup.bank_acc_name.success",
        CLICK_OPEN_MOMO_APP: "zqrbanking.click.btn.open.momo.app",
        OPEN_MOMO_APP_SUCCESS: "zqrbanking.open.momo.app.success",
        FEEDBACK_BANKCARD_CSC: "zqrbanking.feedback.bank_card_csc",
        CLICK_ICON_SHOW_AUTOFILL: "zqrbanking.click.icon.show.autofill",
        CLICK_BANNER_SHOW_AUTOFILL: "zqrbanking.click.banner.show.autofill",
        CLICK_CLOSE_BANNER_AUTOFILL: "zqrbanking.click.close.banner.autofill"
    },
    _ = (e, n) => {
        const i = {
            action: e
        };
        n && (i.data = n), fetch("/log/banking", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            },
            body: G5(i)
        }).catch(C => {
            O.log("SendLog Error", C)
        })
    },
    K = {
        pageLoadDone: e => _(v.PAGE_LOAD_DONE, e),
        clickBtnSaveToQRWallet: e => _(v.CLICK_BUTTON_SAVE_TO_QRWALLET, e),
        clickBtnDone: () => _(v.CLICK_BUTTON_DONE),
        clickBtnOpenBankingApp: () => _(v.CLICK_BUTTON_OPEN_BANKING_APP),
        clickBtnCopy: e => _(v.CLICK_BUTTON_COPY, e),
        clickInputSearch: () => _(v.CLICK_INPUT_SEARCH),
        clickItemBankingApp: e => _(v.CLICK_ITEM_BANKING_APP, e),
        openBankingAppSuccess: e => _(v.OPEN_BANKING_APP_SUCCESS, e),
        clickBannerQRWallet: e => _(v.CLICK_BANNER_QRWALLET, e),
        clickDisclaimer: () => _(v.CLICK_DISCLAIMER),
        autoShowDisclaimer: () => _(v.CLICK_DISCLAIMER, {
            auto: !0
        }),
        clickBtnViewAll: () => _(v.CLICK_BUTTON_VIEW_ALL),
        lookupBankAccountNameSuccess: e => _(v.LOOKUP_BANK_ACC_NAME_SUCCESS, e),
        clickOpenMomoApp: () => _(v.CLICK_OPEN_MOMO_APP),
        openMomoAppSuccess: () => _(v.OPEN_MOMO_APP_SUCCESS),
        feedbackBankCardCSC: e => _(v.FEEDBACK_BANKCARD_CSC, e),
        clickIconShowAutofill: () => _(v.CLICK_ICON_SHOW_AUTOFILL),
        clickBannerShowAutofill: () => _(v.CLICK_BANNER_SHOW_AUTOFILL),
        clickCloseBannerAutofill: () => _(v.CLICK_CLOSE_BANNER_AUTOFILL)
    },
    W5 = "/static/banking/assets/kiss.53a5c854.svg",
    F5 = "/static/banking/assets/love.bdfd93b5.svg",
    q5 = "/static/banking/assets/scared.6e0157bf.svg",
    X5 = "/static/banking/assets/smile.8a6e7291.svg",
    Y5 = "/static/banking/assets/unhappy.540f9feb.svg",
    J5 = "/static/banking/assets/bank-card-csc.9c8525ed.png",
    e3 = [{
        score: 1,
        label: "feedback.bankCSC.q1.opt1",
        emoji: q5
    }, {
        score: 2,
        label: "feedback.bankCSC.q1.opt2",
        emoji: Y5
    }, {
        score: 3,
        label: "feedback.bankCSC.q1.opt3",
        emoji: X5
    }, {
        score: 4,
        label: "feedback.bankCSC.q1.opt4",
        emoji: W5
    }, {
        score: 5,
        label: "feedback.bankCSC.q1.opt5",
        emoji: F5
    }],
    I1 = p5(),
    n3 = () => {
        const {
            t: e
        } = j();
        h1(e("header.feedback"));
        const [n, i] = p.useState(1), [C, r] = p.useState(), [a, s] = p.useState(), l = p.useCallback(m => {
            K.feedbackBankCardCSC({
                sessionId: I1,
                step: 1,
                question1: m.score
            }), r(m), i(2)
        }, []), c = p.useCallback(() => {
            C && (K.feedbackBankCardCSC({
                sessionId: I1,
                step: 2,
                question1: C.score,
                question2: a || ""
            }), i(3))
        }, [C, a]), d = p.useCallback(m => {
            C && (K.feedbackBankCardCSC({
                sessionId: I1,
                step: 3,
                question1: C.score,
                question2: a || "",
                question3: m
            }), i(4))
        }, [C, a]), g = p.useMemo(() => t.jsxs(u, {
            px: 4,
            py: 6,
            children: [t.jsx(u, {
                mb: 4,
                children: t.jsxs($, {
                    align: "center",
                    size: "xxSmall",
                    color: "text-02",
                    children: [e("label.question"), " 1/3"]
                })
            }), t.jsxs(S1, {
                children: [t.jsx(o1, {
                    align: "center",
                    children: e("feedback.bankCSC.q1.title")
                }), t.jsx(u, {
                    mt: 4,
                    children: e3.map(m => t.jsxs(H1, {
                        onClick: () => l(m),
                        children: [t.jsx(u, {
                            mr: 2,
                            children: e(m.label)
                        }), t.jsx("img", {
                            src: m.emoji,
                            alt: e(m.label),
                            width: "20"
                        })]
                    }, m.score))
                })]
            })]
        }), [l, e]), I = p.useMemo(() => {
            var m, b;
            return t.jsxs(u, {
                px: 4,
                py: 6,
                children: [t.jsx(u, {
                    mb: 4,
                    children: t.jsxs($, {
                        align: "center",
                        size: "xxSmall",
                        color: "text-02",
                        children: [e("label.question"), " 2/3"]
                    })
                }), t.jsxs(S1, {
                    children: [t.jsx(u, {
                        children: t.jsxs(o1, {
                            align: "center",
                            children: [e("feedback.bankCSC.q2.title", {
                                answer: (b = e((m = C == null ? void 0 : C.label) != null ? m : "")) == null ? void 0 : b.toLocaleLowerCase()
                            }), t.jsx("img", {
                                style: {
                                    marginLeft: 4,
                                    transform: "translateY(4px)"
                                },
                                src: C == null ? void 0 : C.emoji,
                                alt: C == null ? void 0 : C.label,
                                width: "20"
                            })]
                        })
                    }), t.jsx(u, {
                        my: 4,
                        children: t.jsx(K1.TextArea, {
                            value: a,
                            onChange: B => s(B.target.value),
                            placeholder: e("label.enterYourFeedback")
                        })
                    }), t.jsx(U, {
                        size: "large",
                        fullWidth: !0,
                        onClick: c,
                        children: e("button.continue")
                    })]
                })]
            })
        }, [c, C, a, e]), y = p.useMemo(() => t.jsxs(u, {
            px: 4,
            py: 6,
            children: [t.jsx(u, {
                mb: 4,
                children: t.jsxs($, {
                    align: "center",
                    size: "xxSmall",
                    color: "text-02",
                    children: [e("label.question"), " 3/3"]
                })
            }), t.jsxs(S1, {
                children: [t.jsx(u, {
                    mb: 4,
                    flex: !0,
                    justifyContent: "center",
                    children: t.jsx("img", {
                        src: J5,
                        alt: "Bank card CSC",
                        width: "220px",
                        height: "164px"
                    })
                }), t.jsx(o1, {
                    align: "center",
                    children: e("feedback.bankCSC.q3.title")
                }), t.jsxs(u, {
                    mt: 4,
                    children: [t.jsxs(H1, {
                        onClick: () => d("yes"),
                        children: [t.jsx(n1, {
                            icon: "zi-check",
                            style: {
                                color: "#34B764"
                            }
                        }), t.jsx(u, {
                            ml: 2,
                            children: e("feedback.bankCSC.q3.opt1")
                        })]
                    }), t.jsxs(H1, {
                        onClick: () => d("no"),
                        children: [t.jsx(n1, {
                            icon: "zi-close",
                            style: {
                                color: "#DC1F18"
                            }
                        }), t.jsx(u, {
                            ml: 2,
                            children: e("feedback.bankCSC.q3.opt2")
                        })]
                    })]
                })]
            })]
        }), [e, d]);
        return t.jsx(X, {
            children: t.jsx(r1, {
                bgGray: !0,
                children: t.jsxs(I5, {
                    shadow: !0,
                    children: [n === 1 && g, n === 2 && I, n === 3 && y, n === 4 && t.jsx(t3, {})]
                })
            })
        })
    },
    t3 = () => {
        const {
            t: e
        } = j(), n = p.useCallback(() => {
            T.closeWebview()
        }, []);
        return t.jsxs(u, {
            px: 4,
            py: 6,
            children: [t.jsx(u, {
                mb: 6,
                children: t.jsx(u, {
                    textAlign: "center",
                    style: {
                        marginTop: 56
                    },
                    children: t.jsx(E5, {
                        children: t.jsx(v5, {
                            size: 56
                        })
                    })
                })
            }), t.jsx($, {
                align: "center",
                children: e("feedback.bankCSC.thanks")
            }), t.jsx(u, {
                mt: 6,
                style: {
                    marginBottom: 56
                },
                children: t.jsx(U, {
                    size: "large",
                    fullWidth: !0,
                    onClick: n,
                    children: e("button.finish")
                })
            })]
        })
    },
    a1 = {
        type: "ewallet",
        key: "zalopay",
        code: "zalopay",
        name: "VÃ­ Ä‘iá»‡n tá»­ ZaloPay",
        shortName: "ZaloPay",
        openUrl: "https://social.zalopay.vn/spa/v2/ibft?viet_qr_code=",
        keywords: "zalo, pay, zalopay, zlp"
    },
    o3 = "/assets/",
    B1 = e => {
        const {
            app: n,
            size: i = 24,
            radius: C = 0
        } = e;
        return n === a1.key ? t.jsx(G1, {
            size: i,
            radius: C,
            children: t.jsx(R5, {
                size: i
            })
        }) : t.jsx(G1, {
            size: i,
            radius: C,
            children: t.jsx("img", {
                src: "".concat(o3).concat(n, "-logo.png"),
                draggable: "false",
                alt: n,
                loading: "lazy"
            })
        })
    };
var b2;
const G1 = V.div(b2 || (b2 = k(["\n  box-sizing: border-box;\n  overflow: hidden;\n  width: ", "px;\n  height: ", "px;\n  border-radius: ", "px;\n  overflow: hidden;\n\n  div {\n    transform: ", ";\n    transform-origin: top left;\n  }\n\n  img {\n    width: ", "px;\n    height: ", "px;\n  }\n"])), e => e.size || "32", e => e.size || "32", e => e.radius || "0", e => "scale(calc(".concat(e.size || "32", " / 72))"), e => e.size || "32", e => e.size || "32"),
    D2 = () => {
        const {
            t: e
        } = j();
        return t.jsx(i3, {
            children: t.jsx("div", {
                children: e("message.contentInvalid")
            })
        })
    };
var g2;
const i3 = V.div(g2 || (g2 = k(["\n  box-sizing: border-box;\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100vh;\n"])));

function z2(e) {
    return u5.Buffer.from(e).toString("base64")
}
const s3 = ({
        name: e,
        amount: n,
        phone: i,
        content: C = ""
    }) => {
        const r = z2(JSON.stringify({
                name: e,
                amount: n,
                message: C,
                userId: i
            })),
            a = JSON.stringify({
                dataExtract: r
            }),
            s = encodeURIComponent(JSON.stringify(a)),
            l = "refId=TransferInputMoney&serviceCode=transfer_p2p&action=p2p&extra=".concat(s),
            c = "momo://app?".concat(l);
        T.openOutApp(c, d => {
            if (O.log("openOutApp Momo callback data", d), d.error_code < 0) throw d.js_error || d
        })
    },
    m1 = d5(e => ({
        qrContent: null,
        isOpeningBankApp: !1,
        isOpeningMomoApp: !1,
        setIsOpeningBankApp: n => e({
            isOpeningBankApp: n
        }),
        setIsOpeningMomoApp: n => e({
            isOpeningMomoApp: n
        }),
        loadQRContent: async n => {
            const i = n == null ? void 0 : n.replace(/\+/g, " ");
            i && i1.setItem($1, i);
            const C = i || i1.getItem($1) || "";
            e({
                qrContent: C
            })
        }
    })),
    U2 = () => {
        const e = p.useRef(),
            [n, i] = m1(a => [a.isOpeningMomoApp, a.setIsOpeningMomoApp]),
            C = p.useCallback(a => new Promise((s, l) => {
                e.current && window.cancelAnimationFrame(e.current), s3(a);
                let c = !1,
                    d, g;
                const I = 2e3,
                    y = 500,
                    m = b => {
                        if (d || (d = b), g || (g = b), b - g > y ? (c = !0, s(!0)) : g = b, !c)
                            if (b - d > I)
                                if (Y()) {
                                    const B = "https://apps.apple.com/us/app/id918751511";
                                    T.openOutApp(B, S => {
                                        S.error_code < 0 ? l(S) : s(!0)
                                    })
                                } else l(new Error("Cannot open this app"));
                        else e.current = window.requestAnimationFrame(m)
                    };
                e.current = window.requestAnimationFrame(m)
            }), []);
        return {
            openApp: p.useCallback(async a => {
                var s, l;
                i(!0);
                try {
                    await C(a.data), (s = a.onSuccess) == null || s.call(a), K.openMomoAppSuccess()
                } catch (c) {
                    (l = a.onError) == null || l.call(a, c)
                } finally {
                    e.current && window.cancelAnimationFrame(e.current), i(!1)
                }
            }, [C, i]),
            isOpening: n
        }
    },
    C3 = () => {
        const e = "kbank.kplusvn://dfwithkplus?token=UFJES285bUJlY1pDWDBHaXhyN3hsT3hCM2gyUXJGbmVJOFlRZi92azBsSzhsbU83R1JxWm9TSWlQVFpiS1hYeQ";
        T.openOutApp(e, n => {
            if (O.log("openOutApp Nam A Bank callback data", n), n.error_code < 0) throw n.js_error || n
        })
    },
    a3 = () => {
        const e = "https://mbank.onelink.me/lK5E";
        T.openOutApp(e, n => {
            if (O.log("openOutApp MSB callback data", e, n), n.error_code < 0) throw n.js_error || n
        })
    },
    $2 = e => {
        const n = "nabTransferMoney",
            i = "ops.namabank.com.vn",
            C = {
                partnerId: "",
                partnerName: "Zalo",
                bankId: e.bankCode,
                accountNumber: e.accountNumber,
                accountName: e.accountName || "",
                amount: e.amount,
                description: e.description
            },
            r = z2(JSON.stringify(C)),
            a = "".concat(n, "://").concat(i, "/?data=").concat(r);
        T.openOutApp(a, s => {
            if (O.log("openOutApp Nam A Bank callback data", s), s.error_code < 0) throw s.js_error || s
        })
    },
    r3 = (e, n) => {
        if (!e) throw new Error("Invalid bank");
        const {
            packageId: i,
            scheme: C
        } = e;
        if (!i || !C || C === "#") throw new Error("Invalid bank packId or scheme");
        const r = encodeURI(n != null ? n : ""),
            a = Y(),
            s = "".concat(C, "://").concat(r),
            l = "intent://view?data=".concat(r, "/#Intent;scheme=").concat(C, ";package=").concat(i, ";end"),
            c = a ? s : l;
        if (a) T.openOutApp(c, d => {
            if (O.log("openOutApp callback data", d), d.error_code < 0) throw d.js_error || d
        });
        else {
            const d = {
                android: {
                    package: i,
                    extUrl: r,
                    url: "market://details?id=".concat(i)
                },
                ios: {
                    itunes_id: 0,
                    scheme_url: s,
                    url: "https://apps.apple.com/us/app/id1227187853"
                }
            };
            T.openApp(d, g => {
                if (O.log("openApp callback data", g), g.error_code < 0) throw g.js_error || g
            })
        }
    },
    W1 = e => {
        const n = e.appScheme,
            i = e.appHost;
        let C = "targetPage=QRPay&source=Zalo&timestamp=".concat(e.timestamp);
        C += "&qrContent=".concat(encodeURIComponent(e.content)), C += "&signature=".concat(encodeURIComponent(e.signature));
        const r = "".concat(n, "://").concat(i, "?").concat(C);
        T.openOutApp(r, a => {
            if (O.log("openBankWithSignature callback data", r, a), a.error_code < 0) throw a.js_error || a
        })
    },
    c3 = async ({
        bin: e,
        accountNumber: n
    }) => {
        const i = new URLSearchParams;
        i.append("bin", e), i.append("accountNumber", n);
        const C = "".concat(O1, "/banking/api/lookup"),
            r = await fetch(C, {
                method: "POST",
                body: i,
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
            });
        if (r.ok) {
            const a = await r.json();
            if (a.err >= 0) return a
        }
        throw new Error(r.statusText)
    }, l3 = async () => {
        const e = "".concat(O1, "/banking/api/suggest-banks"),
            n = await fetch(e, {
                method: "POST"
            });
        if (n.ok) {
            const i = await n.json();
            if (i.err >= 0) return i
        }
        throw new Error(n.statusText)
    }, M1 = async (e, n) => {
        var a;
        const i = "".concat(O1, "/banking/api/sign-data"),
            r = await fetch(i, {
                method: "POST",
                body: JSON.stringify({
                    bank: e,
                    data: n
                }),
                headers: {
                    "Content-Type": "application/json"
                }
            });
        if (r.ok) {
            const s = await r.json();
            if (s.err >= 0) return (a = s.data) == null ? void 0 : a.signature;
            throw new Error("".concat(s.err, ": ").concat(s.msg))
        }
        throw new Error(r.statusText)
    }, p3 = async e => {
        var n;
        return M1(A.BankKey.TECHCOMBANK, {
            qrContent: (n = e.content) != null ? n : "",
            targetPage: "QRPay",
            source: "Zalo",
            timestamp: e.timestamp
        })
    }, G2 = e => {
        const n = "tcb",
            i = "applink";
        let C = "targetPage=QRPay&source=Zalo&timestamp=".concat(e.timestamp);
        C += "&qrContent=".concat(encodeURIComponent(e.content)), e.callbackurl && (C += "&callbackurl=".concat(encodeURIComponent(e.callbackurl))), C += "&signature=".concat(encodeURIComponent(e.signature));
        const r = "".concat(n, "://").concat(i, "?").concat(C);
        T.openOutApp(r, a => {
            if (O.log("openOutApp Techcombank callback data", r, a), a.error_code < 0) throw a.js_error || a
        })
    };
var h = (e => (e.ABBANK = "ABB", e.ACB = "ACB", e.AGRIBANK = "AGRIBANK", e.BAC_A_BANK = "BAB", e.BAOVIET_BANK = "BAOVIETBANK", e.BIDC = "BIDC", e.BIDV = "BID", e.CAKE = "CAKE", e.CBBANK = "VNCB", e.CIMB = "CIMB", e.COOP_BANK = "COOPBANK", e.DBS_BANK = "DBS", e.DONG_A_BANK = "DONGABANK", e.EXIMBANK = "EIB", e.GPBANK = "GPBANK", e.HDBANK = "HDB", e.HONGLEONG_BANK = "HLB", e.HSBC = "HSBC", e.IBK_HCM = "IBKHCM", e.IBK_HN = "IBKHN", e.INDOVINA_BANK = "IVB", e.KASIKORN_BANK = "KBANK", e.KIENLONG_BANK = "KLB", e.KOOKMIN_BANK_HCM = "KBHCM", e.KOOKMIN_BANK_HN = "KBHN", e.LIENVIETPOST_BANK = "LPB", e.MBBANK = "MBB", e.MSB = "MSB", e.NAM_A_BANK = "NAB", e.NCB = "NVB", e.NONGHYUP_BANK_HN = "NONGHYUP", e.OCB = "OCB", e.OCEANBANK = "OCEANBANK", e.PGBANK = "PGB", e.PUBLIC_BANK = "PBVN", e.PVCOM_BANK = "PVCOMBANK", e.SACOMBANK = "STB", e.SAIGONBANK = "SGB", e.SCB = "SCB", e.SEA_BANK = "SSB", e.SHB = "SHB", e.SHINHAN_BANK = "SVB", e.STANDARD_CHARTERED_BANK = "SC", e.TECHCOMBANK = "TCB", e.TIMO = "TIMO", e.TPBANK = "TPB", e.UBANK = "UBANK", e.UNITED_OVERSEAS_BANK = "UOB", e.VIB = "VIB", e.VIET_A_BANK = "VAB", e.VIET_BANK = "VBB", e.VIETCAPITAL_BANK = "BVB", e.VIETCOMBANK = "VCB", e.VIETINBANK = "CTG", e.VPBANK = "VPB", e.VRB = "VRB", e.WOORI_BANK = "WRB", e))(h || {}),
    o = (e => (e.ABBANK = "abbank", e.ACB = "acb", e.AGRIBANK = "agribank", e.BAC_A_BANK = "bacabank", e.BAOVIET_BANK = "baoviet", e.BIDC = "bidc", e.BIDV = "bidv", e.CAKE = "cake", e.CBBANK = "cbbank", e.CIMB = "cimb", e.COOP_BANK = "coopbank", e.DBS_BANK = "dbsbank", e.DONG_A_BANK = "dongabank", e.EXIMBANK = "eximbank", e.GPBANK = "gpbank", e.HDBANK = "hdbank", e.HONGLEONG_BANK = "hongleongbank", e.HSBC = "hsbc", e.IBK_HCM = "ibkhcm", e.IBK_HN = "ibkhn", e.INDOVINA_BANK = "indovinabank", e.KASIKORN_BANK = "kasikorn", e.KIENLONG_BANK = "kienlongbank", e.KOOKMIN_BANK_HCM = "kookminhcm", e.KOOKMIN_BANK_HN = "kookminhn", e.LIENVIETPOST_BANK = "lienvietpostbank", e.MBBANK = "mbbank", e.MSB = "msb", e.NAM_A_BANK = "namabank", e.NCB = "ncb", e.NONGHYUP_BANK_HN = "nonghyup", e.OCB = "ocb", e.OCEANBANK = "oceanbank", e.PGBANK = "pgbank", e.PUBLIC_BANK = "publicbank", e.PVCOM_BANK = "pvcombank", e.SACOMBANK = "sacombank", e.SAIGONBANK = "saigonbank", e.SCB = "scb", e.SEA_BANK = "seabank", e.SHB = "shb", e.SHINHAN_BANK = "shinhanbank", e.STANDARD_CHARTERED_BANK = "standardcharteredbank", e.TECHCOMBANK = "techcombank", e.TIMO = "timo", e.TPBANK = "tpbank", e.UBANK = "ubank", e.UNITED_OVERSEAS_BANK = "uob", e.VIB = "vib", e.VIET_A_BANK = "vietabank", e.VIET_BANK = "vietbank", e.VIETCAPITAL_BANK = "banviet", e.VIETCOMBANK = "vietcombank", e.VIETINBANK = "vietinbank", e.VPBANK = "vpbank", e.VRB = "vrb", e.WOORI_BANK = "wooribank", e))(o || {});
const W2 = {
        [o.ABBANK]: {
            key: o.ABBANK,
            code: h.ABBANK,
            name: "NgÃ¢n hÃ ng TMCP An BÃ¬nh",
            bin: "970425",
            shortName: "AB Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "ABBKVNVX",
            keywords: "anbinh"
        },
        [o.ACB]: {
            key: o.ACB,
            code: h.ACB,
            name: "NgÃ¢n hÃ ng TMCP Ã ChÃ¢u",
            bin: "970416",
            shortName: "ACB",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "ASCBVNVX",
            keywords: "achau"
        },
        [o.AGRIBANK]: {
            key: o.AGRIBANK,
            code: h.AGRIBANK,
            name: "NgÃ¢n hÃ ng NÃ´ng nghiá»‡p vÃ  PhÃ¡t triá»ƒn NÃ´ng thÃ´n Viá»‡t Nam",
            bin: "970405",
            shortName: "Agribank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VBAAVNVX",
            keywords: "nongnghiep, nongthon, agribank, agri"
        },
        [o.BAC_A_BANK]: {
            key: o.BAC_A_BANK,
            code: h.BAC_A_BANK,
            name: "NgÃ¢n hÃ ng TMCP Báº¯c Ã",
            bin: "970409",
            shortName: "BacA Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "NASCVNVX",
            keywords: "baca, NASB"
        },
        [o.BAOVIET_BANK]: {
            key: o.BAOVIET_BANK,
            code: h.BAOVIET_BANK,
            name: "NgÃ¢n hÃ ng TMCP Báº£o Viá»‡t",
            bin: "970438",
            shortName: "BaoViet Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "BVBVVNVX",
            keywords: "baoviet, BVB"
        },
        [o.BIDC]: {
            key: o.BIDC,
            code: h.BIDC,
            name: "NgÃ¢n hÃ ng TMCP Äáº§u tÆ° vÃ  PhÃ¡t triá»ƒn Campuchia",
            bin: "",
            shortName: "BIDC",
            vietQRStatus: -1
        },
        [o.BIDV]: {
            key: o.BIDV,
            code: h.BIDV,
            name: "NgÃ¢n hÃ ng TMCP Äáº§u tÆ° vÃ  PhÃ¡t triá»ƒn Viá»‡t Nam",
            bin: "970418",
            shortName: "BIDV",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "BIDVVNVX"
        },
        [o.CAKE]: {
            key: o.CAKE,
            code: h.CAKE,
            name: "NgÃ¢n hÃ ng sá»‘ CAKE by VPBank - NgÃ¢n hÃ ng TMCP Viá»‡t Nam Thá»‹nh VÆ°á»£ng",
            bin: "546034",
            shortName: "CAKE by VPBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: null
        },
        [o.CBBANK]: {
            key: o.CBBANK,
            code: h.CBBANK,
            name: "NgÃ¢n hÃ ng ThÆ°Æ¡ng máº¡i TNHH MTV XÃ¢y dá»±ng Viá»‡t Nam",
            bin: "970444",
            shortName: "CB Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "GTBAVNVX",
            keywords: "xaydungvn, xaydung"
        },
        [o.CIMB]: {
            key: o.CIMB,
            code: h.CIMB,
            name: "NgÃ¢n hÃ ng TNHH MTV CIMB Viá»‡t Nam",
            bin: "422589",
            shortName: "CIMB Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "CIBBVNVN",
            keywords: "cimbvn"
        },
        [o.COOP_BANK]: {
            key: o.COOP_BANK,
            code: h.COOP_BANK,
            name: "NgÃ¢n hÃ ng Há»£p tÃ¡c xÃ£ Viá»‡t Nam",
            bin: "970446",
            shortName: "Co-op Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: null,
            keywords: "hoptacxa, coop"
        },
        [o.DBS_BANK]: {
            key: o.DBS_BANK,
            code: h.DBS_BANK,
            name: "NH TNHH MTV PhÃ¡t triá»ƒn Singapore - Chi nhÃ¡nh TP. Há»“ ChÃ­ Minh",
            bin: "796500",
            shortName: "DBS Bank",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: "DBSSVNVX",
            keywords: "dbshcm"
        },
        [o.DONG_A_BANK]: {
            key: o.DONG_A_BANK,
            code: h.DONG_A_BANK,
            name: "NgÃ¢n hÃ ng TMCP ÄÃ´ng Ã",
            bin: "970406",
            shortName: "DongA Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "EACBVNVX",
            keywords: "donga, DAB"
        },
        [o.EXIMBANK]: {
            key: o.EXIMBANK,
            code: h.EXIMBANK,
            name: "NgÃ¢n hÃ ng TMCP Xuáº¥t Nháº­p kháº©u Viá»‡t Nam",
            bin: "970431",
            shortName: "Eximbank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "EBVIVNVX"
        },
        [o.GPBANK]: {
            key: o.GPBANK,
            code: h.GPBANK,
            name: "NgÃ¢n hÃ ng ThÆ°Æ¡ng máº¡i TNHH MTV Dáº§u KhÃ­ ToÃ n Cáº§u",
            bin: "970408",
            shortName: "GPBank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "GBNKVNVX",
            keywords: "daukhi"
        },
        [o.HDBANK]: {
            key: o.HDBANK,
            code: h.HDBANK,
            name: "NgÃ¢n hÃ ng TMCP PhÃ¡t triá»ƒn TP. Há»“ ChÃ­ Minh",
            bin: "970437",
            shortName: "HDBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "HDBCVNVX"
        },
        [o.HONGLEONG_BANK]: {
            key: o.HONGLEONG_BANK,
            code: h.HONGLEONG_BANK,
            name: "NgÃ¢n hÃ ng TNHH MTV Hong Leong Viá»‡t Nam",
            bin: "970442",
            shortName: "HongLeong Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "HLBBVNVX",
            keywords: "HLBVN"
        },
        [o.HSBC]: {
            key: o.HSBC,
            code: h.HSBC,
            name: "NgÃ¢n hÃ ng TNHH MTV HSBC (Viá»‡t Nam)",
            bin: "458761",
            shortName: "HSBC Vietnam",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "HSBCVNVX"
        },
        [o.IBK_HCM]: {
            key: o.IBK_HCM,
            code: h.IBK_HCM,
            name: "NgÃ¢n hÃ ng CÃ´ng nghiá»‡p HÃ n Quá»‘c - Chi nhÃ¡nh TP. Há»“ ChÃ­ Minh",
            bin: "970456",
            shortName: "IBK HCM",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: null,
            keywords: "congnghiep"
        },
        [o.IBK_HN]: {
            key: o.IBK_HN,
            code: h.IBK_HN,
            name: "NgÃ¢n hÃ ng CÃ´ng nghiá»‡p HÃ n Quá»‘c - Chi nhÃ¡nh HÃ  Ná»™i",
            bin: "970455",
            shortName: "IBK HN",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: null,
            keywords: "congnghiep"
        },
        [o.INDOVINA_BANK]: {
            key: o.INDOVINA_BANK,
            code: h.INDOVINA_BANK,
            name: "NgÃ¢n hÃ ng TNHH Indovina",
            bin: "970434",
            shortName: "Indovina Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: null
        },
        [o.KASIKORN_BANK]: {
            key: o.KASIKORN_BANK,
            code: h.KASIKORN_BANK,
            name: "NgÃ¢n hÃ ng Äáº¡i chÃºng TNHH KASIKORNBANK - CN TP. Há»“ ChÃ­ Minh",
            bin: "668888",
            shortName: "Kasikornbank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "KASIVNVX"
        },
        [o.KIENLONG_BANK]: {
            key: o.KIENLONG_BANK,
            code: h.KIENLONG_BANK,
            name: "NgÃ¢n hÃ ng TMCP KiÃªn Long",
            bin: "970452",
            shortName: "KienlongBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "KLBKVNVX"
        },
        [o.KOOKMIN_BANK_HCM]: {
            key: o.KOOKMIN_BANK_HCM,
            code: h.KOOKMIN_BANK_HCM,
            name: "NgÃ¢n hÃ ng Kookmin - Chi nhÃ¡nh TP. Há»“ ChÃ­ Minh",
            bin: "970463",
            shortName: "Kookmin Bank HCM",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: null
        },
        [o.KOOKMIN_BANK_HN]: {
            key: o.KOOKMIN_BANK_HN,
            code: h.KOOKMIN_BANK_HN,
            name: "NgÃ¢n hÃ ng Kookmin - Chi nhÃ¡nh HÃ  Ná»™i",
            bin: "970462",
            shortName: "Kookmin Bank HN",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: null
        },
        [o.LIENVIETPOST_BANK]: {
            key: o.LIENVIETPOST_BANK,
            code: h.LIENVIETPOST_BANK,
            name: "NgÃ¢n hÃ ng TMCP BÆ°u Äiá»‡n LiÃªn Viá»‡t",
            bin: "970449",
            shortName: "LienVietPostBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "LVBKVNVX",
            keywords: "lienvietbank"
        },
        [o.MBBANK]: {
            key: o.MBBANK,
            code: h.MBBANK,
            name: "NgÃ¢n hÃ ng TMCP QuÃ¢n Ä‘á»™i",
            bin: "970422",
            shortName: "MB Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "MSCBVNVX"
        },
        [o.MSB]: {
            key: o.MSB,
            code: h.MSB,
            name: "NgÃ¢n hÃ ng TMCP HÃ ng Háº£i",
            bin: "970426",
            shortName: "MSB",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "MCOBVNVX",
            keywords: "hanghai"
        },
        [o.NAM_A_BANK]: {
            key: o.NAM_A_BANK,
            code: h.NAM_A_BANK,
            name: "NgÃ¢n hÃ ng TMCP Nam Ã",
            bin: "970428",
            shortName: "Nam A Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "NAMAVNVX",
            keywords: "namabank"
        },
        [o.NCB]: {
            key: o.NCB,
            code: h.NCB,
            name: "NgÃ¢n hÃ ng TMCP Quá»‘c DÃ¢n",
            bin: "970419",
            shortName: "NCB Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "NVBAVNVX",
            keywords: "quocdan"
        },
        [o.NONGHYUP_BANK_HN]: {
            key: o.NONGHYUP_BANK_HN,
            code: h.NONGHYUP_BANK_HN,
            name: "NgÃ¢n hÃ ng Nonghyup - Chi nhÃ¡nh HÃ  Ná»™i",
            bin: "801011",
            shortName: "Nonghyup Bank",
            vietQRStatus: 0,
            lookupSupported: 0,
            swiftCode: null
        },
        [o.OCB]: {
            key: o.OCB,
            code: h.OCB,
            name: "NgÃ¢n hÃ ng TMCP PhÆ°Æ¡ng ÄÃ´ng",
            bin: "970448",
            shortName: "OCB Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "ORCOVNVX",
            keywords: "phuongdong"
        },
        [o.OCEANBANK]: {
            key: o.OCEANBANK,
            code: h.OCEANBANK,
            name: "NgÃ¢n hÃ ng ThÆ°Æ¡ng máº¡i TNHH MTV Äáº¡i DÆ°Æ¡ng",
            bin: "970414",
            shortName: "Ocean Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "OCBKUS3M",
            keywords: "daiduong"
        },
        [o.PGBANK]: {
            key: o.PGBANK,
            code: h.PGBANK,
            name: "NgÃ¢n hÃ ng TMCP XÄƒng dáº§u Petrolimex",
            bin: "970430",
            shortName: "PG Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "PGBLVNVX"
        },
        [o.PUBLIC_BANK]: {
            key: o.PUBLIC_BANK,
            code: h.PUBLIC_BANK,
            name: "NgÃ¢n hÃ ng TNHH MTV Public Viá»‡t Nam",
            bin: "970439",
            shortName: "Public Bank Vietnam",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "VIDPVNVX",
            keywords: "publicvn"
        },
        [o.PVCOM_BANK]: {
            key: o.PVCOM_BANK,
            code: h.PVCOM_BANK,
            name: "NgÃ¢n hÃ ng TMCP Äáº¡i ChÃºng Viá»‡t Nam",
            bin: "970412",
            shortName: "PVcomBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "WBVNVNVX",
            keywords: "daichung"
        },
        [o.SACOMBANK]: {
            key: o.SACOMBANK,
            code: h.SACOMBANK,
            name: "NgÃ¢n hÃ ng TMCP SÃ i GÃ²n ThÆ°Æ¡ng TÃ­n",
            bin: "970403",
            shortName: "Sacombank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SGTTVNVX"
        },
        [o.SAIGONBANK]: {
            key: o.SAIGONBANK,
            code: h.SAIGONBANK,
            name: "NgÃ¢n hÃ ng TMCP SÃ i GÃ²n CÃ´ng ThÆ°Æ¡ng",
            bin: "970400",
            shortName: "SaigonBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SBITVNVX",
            keywords: "saigoncongthuong, saigonbank"
        },
        [o.SCB]: {
            key: o.SCB,
            code: h.SCB,
            name: "NgÃ¢n hÃ ng TMCP SÃ i GÃ²n",
            bin: "970429",
            shortName: "SCB",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SACLVNVX",
            keywords: "saigon"
        },
        [o.SEA_BANK]: {
            key: o.SEA_BANK,
            code: h.SEA_BANK,
            name: "NgÃ¢n hÃ ng TMCP ÄÃ´ng Nam Ã",
            bin: "970440",
            shortName: "SeABank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SEAVVNVX"
        },
        [o.SHB]: {
            key: o.SHB,
            code: h.SHB,
            name: "NgÃ¢n hÃ ng TMCP SÃ i GÃ²n - HÃ  Ná»™i",
            bin: "970443",
            shortName: "SHB",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SHBAVNVX",
            keywords: "saigonhanoi, sghn"
        },
        [o.SHINHAN_BANK]: {
            key: o.SHINHAN_BANK,
            code: h.SHINHAN_BANK,
            name: "NgÃ¢n hÃ ng TNHH MTV Shinhan Viá»‡t Nam",
            bin: "970424",
            shortName: "Shinhan Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "SHBKVNVX"
        },
        [o.STANDARD_CHARTERED_BANK]: {
            key: o.STANDARD_CHARTERED_BANK,
            code: h.STANDARD_CHARTERED_BANK,
            name: "NgÃ¢n hÃ ng TNHH MTV Standard Chartered Bank Viá»‡t Nam",
            bin: "970410",
            shortName: "Standard Chartered Vietnam",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: "SCBLVNVX"
        },
        [o.TECHCOMBANK]: {
            key: o.TECHCOMBANK,
            code: h.TECHCOMBANK,
            name: "NgÃ¢n hÃ ng TMCP Ká»¹ thÆ°Æ¡ng Viá»‡t Nam",
            bin: "970407",
            shortName: "Techcombank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VTCBVNVX"
        },
        [o.TIMO]: {
            key: o.TIMO,
            code: h.TIMO,
            name: "NgÃ¢n hÃ ng sá»‘ Timo by Báº£n Viá»‡t Bank",
            bin: "963388",
            shortName: "Timo",
            vietQRStatus: 1,
            lookupSupported: 0,
            swiftCode: null,
            keywords: "banviet"
        },
        [o.TPBANK]: {
            key: o.TPBANK,
            code: h.TPBANK,
            name: "NgÃ¢n hÃ ng TMCP TiÃªn Phong",
            bin: "970423",
            shortName: "TPBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "TPBVVNVX",
            keywords: "tienphong"
        },
        [o.UBANK]: {
            key: o.UBANK,
            code: h.UBANK,
            name: "NgÃ¢n hÃ ng sá»‘ Ubank by VPBank - NgÃ¢n hÃ ng TMCP Viá»‡t Nam Thá»‹nh VÆ°á»£ng",
            bin: "546035",
            shortName: "Ubank by VPBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: null
        },
        [o.UNITED_OVERSEAS_BANK]: {
            key: o.UNITED_OVERSEAS_BANK,
            code: h.UNITED_OVERSEAS_BANK,
            name: "NgÃ¢n hÃ ng United Overseas Bank Viá»‡t Nam",
            bin: "970458",
            shortName: "United Overseas Bank Vietnam",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: null
        },
        [o.VIB]: {
            key: o.VIB,
            code: h.VIB,
            name: "NgÃ¢n hÃ ng TMCP Quá»‘c táº¿ Viá»‡t Nam",
            bin: "970441",
            shortName: "VIB",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VNIBVNVX",
            keywords: "quocte"
        },
        [o.VIET_A_BANK]: {
            key: o.VIET_A_BANK,
            code: h.VIET_A_BANK,
            name: "NgÃ¢n hÃ ng TMCP Viá»‡t Ã",
            bin: "970427",
            shortName: "VietABank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VNACVNVX"
        },
        [o.VIET_BANK]: {
            key: o.VIET_BANK,
            code: h.VIET_BANK,
            name: "NgÃ¢n hÃ ng TMCP Viá»‡t Nam ThÆ°Æ¡ng TÃ­n",
            bin: "970433",
            shortName: "VietBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VNTTVNVX",
            keywords: "vietnamthuongtin, vnthuongtin"
        },
        [o.VIETCAPITAL_BANK]: {
            key: o.VIETCAPITAL_BANK,
            code: h.VIETCAPITAL_BANK,
            name: "NgÃ¢n hÃ ng TMCP Báº£n Viá»‡t",
            bin: "970454",
            shortName: "Viet Capital Bank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VCBCVNVX",
            keywords: "banviet"
        },
        [o.VIETCOMBANK]: {
            key: o.VIETCOMBANK,
            code: h.VIETCOMBANK,
            name: "NgÃ¢n hÃ ng TMCP Ngoáº¡i ThÆ°Æ¡ng Viá»‡t Nam",
            bin: "970436",
            shortName: "Vietcombank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "BFTVVNVX"
        },
        [o.VIETINBANK]: {
            key: o.VIETINBANK,
            code: h.VIETINBANK,
            name: "NgÃ¢n hÃ ng TMCP CÃ´ng thÆ°Æ¡ng Viá»‡t Nam",
            bin: "970415",
            shortName: "VietinBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "ICBVVNVX",
            keywords: "viettin"
        },
        [o.VPBANK]: {
            key: o.VPBANK,
            code: h.VPBANK,
            name: "NgÃ¢n hÃ ng TMCP Viá»‡t Nam Thá»‹nh VÆ°á»£ng",
            bin: "970432",
            shortName: "VPBank",
            vietQRStatus: 1,
            lookupSupported: 1,
            swiftCode: "VPBKVNVX",
            keywords: "vnthinhvuong"
        },
        [o.VRB]: {
            key: o.VRB,
            code: h.VRB,
            name: "NgÃ¢n hÃ ng LiÃªn doanh Viá»‡t - Nga",
            bin: "970421",
            shortName: "VietNgaBank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: null,
            keywords: "vietnam-russia, vrbank"
        },
        [o.WOORI_BANK]: {
            key: o.WOORI_BANK,
            code: h.WOORI_BANK,
            name: "NgÃ¢n hÃ ng TNHH MTV Woori Viá»‡t Nam",
            bin: "970457",
            shortName: "Woori Bank",
            vietQRStatus: 0,
            lookupSupported: 1,
            swiftCode: null
        }
    },
    u3 = Object.values(W2),
    d3 = u3,
    h3 = W2,
    T1 = e => d3.find(n => n.bin === e),
    m3 = [o.DBS_BANK, o.HSBC, o.KOOKMIN_BANK_HCM, o.KOOKMIN_BANK_HN, o.KASIKORN_BANK, o.NONGHYUP_BANK_HN, o.UNITED_OVERSEAS_BANK, o.UBANK, o.CAKE, o.STANDARD_CHARTERED_BANK, o.TIMO],
    j1 = (e, n) => {
        const i = p.useRef(!1);
        p.useEffect(() => {
            !i.current && n && (i.current = !0, e())
        }, [e, n])
    },
    b1 = () => {
        const [e] = m1(r => [r.qrContent]), n = p.useMemo(() => {
            const r = new A.QRPay(e != null ? e : "");
            return r.provider.guid === "908405" && (r.provider.name = A.QRProvider.VNPAY), r
        }, [e]), i = p.useMemo(() => {
            var a, s, l, c, d, g, I;
            return n.isValid ? {
                type: (a = n == null ? void 0 : n.provider) == null ? void 0 : a.name,
                service: (s = n == null ? void 0 : n.provider) == null ? void 0 : s.service,
                bank: T1((l = n.consumer) == null ? void 0 : l.bankBin),
                bankNumber: (c = n.consumer) == null ? void 0 : c.bankNumber,
                amount: n == null ? void 0 : n.amount,
                content: (d = n.additionalData) == null ? void 0 : d.purpose,
                store: (g = n.additionalData) == null ? void 0 : g.store,
                terminal: (I = n.additionalData) == null ? void 0 : I.terminal
            } : null
        }, [n]), C = p.useMemo(() => !n.isValid || !n.provider.name ? !1 : n.provider.name === A.QRProvider.VIETQR && i != null && i.bank ? !0 : n.provider.name === A.QRProvider.VNPAY ? !!n.additionalData.store : !1, [n, i]);
        return j1(() => {
            i && O.log("data", i)
        }, !!i), {
            data: i,
            qrPay: n,
            isSupported: C,
            qrContent: e
        }
    },
    P1 = () => {
        const e = p.useRef();
        return async n => new Promise((i, C) => {
            e.current && window.cancelAnimationFrame(e.current), n();
            let r = !1,
                a, s;
            const l = 3e3,
                c = 500,
                d = g => {
                    a || (a = g), s || (s = g), g - s > c ? (r = !0, i(!0)) : s = g, r || (g - a > l ? C(new Error("Open timeout")) : e.current = window.requestAnimationFrame(d))
                };
            e.current = window.requestAnimationFrame(d)
        })
    },
    F2 = () => {
        const {
            qrContent: e,
            qrPay: n
        } = b1(), [i, C] = m1(l => [l.isOpeningBankApp, l.setIsOpeningBankApp]), r = P1(), a = p.useCallback(async l => {
            const c = String(Date.now());
            let d = "";
            if (l.key === A.BankKey.TECHCOMBANK) try {
                d = await p3({
                    content: e != null ? e : "",
                    timestamp: String(Date.now())
                })
            } catch (g) {
                O.log("buildSignature error", g)
            }
            return new Promise((g, I) => {
                r(() => {
                    var y, m, b, B;
                    if (l.key === A.BankKey.NAM_A_BANK && ((y = n == null ? void 0 : n.consumer) != null && y.bankBin) && ((m = n.consumer) != null && m.bankNumber)) $2({
                        bankCode: (b = n == null ? void 0 : n.consumer) == null ? void 0 : b.bankBin,
                        accountNumber: (B = n.consumer) == null ? void 0 : B.bankNumber,
                        amount: (n == null ? void 0 : n.amount) || "",
                        description: (n == null ? void 0 : n.additionalData.purpose) || ""
                    });
                    else if (l.key === A.BankKey.TECHCOMBANK && d) G2({
                        content: e != null ? e : "",
                        timestamp: c,
                        signature: d
                    });
                    else if (l.key === A.BankKey.MSB) a3();
                    else if (l.key === A.BankKey.KASIKORN_BANK) C3();
                    else {
                        const S = n.provider.name === A.QRProvider.VIETQR ? "" : e;
                        r3(l, S != null ? S : "")
                    }
                }).then(() => {
                    g({
                        openStore: !1
                    })
                }).catch(y => {
                    if (l != null && l.appStoreId && Y()) {
                        const m = "https://apps.apple.com/us/app/".concat(l.appStoreId);
                        T.openOutApp(m, b => {
                            b.error_code < 0 ? I(b) : g({
                                openStore: !0
                            })
                        })
                    } else l.packageId && !Y() ? T.openOutApp("market://details?id=".concat(l.packageId), m => {
                        m.error_code < 0 ? I(m) : g({
                            openStore: !0
                        })
                    }) : I(y)
                })
            })
        }, [e, r, n]), s = p.useCallback((l, c) => {
            i || !l || (C(!0), a(l).then(d => {
                var g;
                (g = c == null ? void 0 : c.onSuccess) == null || g.call(c, d)
            }).catch(d => {
                var g;
                (g = c == null ? void 0 : c.onError) == null || g.call(c, d)
            }).finally(() => {
                C(!1)
            }))
        }, [i, a, C]);
        return {
            isOpening: i,
            openApp: s
        }
    },
    q2 = e => {
        const n = h5(),
            i = p.useMemo(() => new URLSearchParams(n.search), [n.search]);
        return p.useMemo(() => {
            const r = {};
            return e.forEach(a => {
                r[a] = i.get(a)
            }), r
        }, [i, e])
    },
    b3 = ({
        children: e
    }) => {
        const {
            t: n
        } = j(), {
            isOpening: i
        } = F2(), {
            isOpening: C
        } = U2(), {
            content: r
        } = q2(["content"]), [a, s] = m1(d => [d.qrContent, d.loadQRContent]);
        p.useEffect(() => {
            a === null && s(r)
        }, [a, r, s]);
        const l = p.useMemo(() => i || C, [i, C]),
            c = p.useMemo(() => i ? "label.openingApp" : C ? "label.openingMomoApp" : "label.opening", [i, C]);
        return t.jsxs(t.Fragment, {
            children: [e, t.jsx(f1, {
                visible: l,
                text: n(c)
            })]
        })
    },
    X2 = ({
        src: e,
        type: n,
        bankAccountName: i
    }) => {
        const {
            t: C
        } = j(), {
            utm_source: r
        } = q2(["utm_source"]), {
            data: a
        } = b1(), s = p.useCallback(() => {
            var d;
            K.clickBannerQRWallet({
                src: e,
                type: n
            });
            const l = new URLSearchParams;
            l.append("utm_campaign", "bank_qr_2"), l.append("utm_medium", "h5_banking_banner".concat(n ? "_".concat(n == null ? void 0 : n.toLocaleLowerCase()) : "")), l.append("utm_source", "h5_banking_banner"), (a == null ? void 0 : a.type) === A.QRProvider.VIETQR && (l.append("bank", ((d = a.bank) == null ? void 0 : d.key) || ""), l.append("accountName", i || ""), l.append("accountNumber", a.bankNumber || ""), l.append("isSuggestion", "true"));
            const c = "https://zalo.me/s/2646373759294038927/?".concat(l);
            T.openInApp(c, g => {
                g.error_code < 0 && O.log("openInApp Error", c, g)
            })
        }, [e, n, a, i]);
        return r === "qr_wallet" ? null : t.jsxs(g3, {
            onClick: s,
            children: [t.jsx(u, {
                mr: 2,
                style: {
                    display: "inline-flex"
                },
                children: t.jsxs("svg", {
                    width: "40",
                    height: "40",
                    viewBox: "0 0 40 40",
                    fill: "none",
                    xmlns: "http://www.w3.org/2000/svg",
                    children: [t.jsxs("g", {
                        opacity: "0.75",
                        children: [t.jsxs("g", {
                            opacity: "0.75",
                            children: [t.jsx("circle", {
                                cx: "17.5",
                                cy: "21.5",
                                r: "14.5",
                                fill: "white"
                            }), t.jsx("path", {
                                d: "M14.6019 23.5334H12.1265C12.0125 23.5321 11.8994 23.5535 11.7938 23.5965C11.6882 23.6396 11.5922 23.7032 11.5116 23.7839C11.431 23.8645 11.3673 23.9604 11.3243 24.066C11.2813 24.1716 11.2598 24.2848 11.2612 24.3988V26.8742C11.2598 26.9882 11.2813 27.1013 11.3243 27.2069C11.3673 27.3125 11.431 27.4084 11.5116 27.4891C11.5922 27.5697 11.6882 27.6334 11.7938 27.6764C11.8994 27.7194 12.0125 27.7409 12.1265 27.7395H14.6019C14.7159 27.7409 14.829 27.7194 14.9346 27.6764C15.0402 27.6334 15.1362 27.5697 15.2168 27.4891C15.2974 27.4084 15.3611 27.3125 15.4041 27.2069C15.4471 27.1013 15.4686 26.9882 15.4673 26.8742V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334ZM14.5113 26.3509C14.5113 26.4657 14.4657 26.5757 14.3846 26.6569C14.3035 26.738 14.1934 26.7836 14.0786 26.7836H12.6498C12.535 26.7836 12.425 26.738 12.3438 26.6569C12.2627 26.5757 12.2171 26.4657 12.2171 26.3509V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3509ZM22.8732 15.2822H20.3979C20.2838 15.2809 20.1707 15.3023 20.0651 15.3453C19.9595 15.3883 19.8636 15.452 19.7829 15.5327C19.7023 15.6133 19.6386 15.7092 19.5956 15.8148C19.5526 15.9204 19.5311 16.0336 19.5325 16.1476V18.6229C19.5311 18.737 19.5526 18.8501 19.5956 18.9557C19.6386 19.0613 19.7023 19.1572 19.7829 19.2379C19.8636 19.3185 19.9595 19.3822 20.0651 19.4252C20.1707 19.4682 20.2838 19.4897 20.3979 19.4883H22.8732C22.9872 19.4897 23.1004 19.4682 23.206 19.4252C23.3116 19.3822 23.4075 19.3185 23.4881 19.2379C23.5688 19.1572 23.6325 19.0613 23.6755 18.9557C23.7185 18.8501 23.74 18.737 23.7386 18.6229V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2822ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 15.252H12.1265C12.0125 15.2507 11.8994 15.2721 11.7938 15.3151C11.6882 15.3582 11.5922 15.4218 11.5116 15.5025C11.431 15.5831 11.3673 15.679 11.3243 15.7846C11.2813 15.8902 11.2598 16.0034 11.2612 16.1174V18.5928C11.2598 18.7068 11.2813 18.8199 11.3243 18.9255C11.3673 19.0311 11.431 19.127 11.5116 19.2077C11.5922 19.2883 11.6882 19.352 11.7938 19.395C11.8994 19.438 12.0125 19.4595 12.1265 19.4581H14.6019C14.7159 19.4595 14.829 19.438 14.9346 19.395C15.0402 19.352 15.1362 19.2883 15.2168 19.2077C15.2974 19.127 15.3611 19.0311 15.4041 18.9255C15.4471 18.8199 15.4686 18.7068 15.4673 18.5928V16.1275C15.4686 16.0134 15.4471 15.9003 15.4041 15.7947C15.3611 15.6891 15.2974 15.5932 15.2168 15.5125C15.1362 15.4319 15.0402 15.3682 14.9346 15.3252C14.829 15.2822 14.7159 15.2607 14.6019 15.2621V15.252ZM14.5113 18.0695C14.5088 18.1835 14.4624 18.292 14.3818 18.3726C14.3012 18.4532 14.1926 18.4996 14.0786 18.5022H12.6498C12.535 18.5022 12.425 18.4566 12.3438 18.3755C12.2627 18.2943 12.2171 18.1843 12.2171 18.0695V16.6507C12.2171 16.5359 12.2627 16.4259 12.3438 16.3447C12.425 16.2636 12.535 16.218 12.6498 16.218H14.0686C14.1833 16.218 14.2934 16.2636 14.3745 16.3447C14.4557 16.4259 14.5013 16.5359 14.5013 16.6507L14.5113 18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 15.2721H12.1265C12.0125 15.2708 11.8994 15.2923 11.7938 15.3353C11.6882 15.3783 11.5922 15.442 11.5116 15.5226C11.431 15.6032 11.3673 15.6992 11.3243 15.8048C11.2813 15.9104 11.2598 16.0235 11.2612 16.1375V18.6129C11.2598 18.7269 11.2813 18.84 11.3243 18.9456C11.3673 19.0512 11.431 19.1472 11.5116 19.2278C11.5922 19.3084 11.6882 19.3721 11.7938 19.4151C11.8994 19.4581 12.0125 19.4796 12.1265 19.4782H14.6019C14.7159 19.4796 14.829 19.4581 14.9346 19.4151C15.0402 19.3721 15.1362 19.3084 15.2168 19.2278C15.2974 19.1472 15.3611 19.0512 15.4041 18.9456C15.4471 18.84 15.4686 18.7269 15.4673 18.6129V16.1275C15.4686 16.0134 15.4471 15.9003 15.4041 15.7947C15.3611 15.6891 15.2974 15.5932 15.2168 15.5125C15.1362 15.4319 15.0402 15.3682 14.9346 15.3252C14.829 15.2822 14.7159 15.2607 14.6019 15.2621V15.2721ZM14.5113 18.0695C14.5088 18.1835 14.4624 18.292 14.3818 18.3726C14.3012 18.4532 14.1926 18.4996 14.0786 18.5022H12.6498C12.535 18.5022 12.425 18.4566 12.3438 18.3755C12.2627 18.2943 12.2171 18.1843 12.2171 18.0695V16.6507C12.2171 16.5359 12.2627 16.4259 12.3438 16.3447C12.425 16.2636 12.535 16.218 12.6498 16.218H14.0686C14.1833 16.218 14.2934 16.2636 14.3745 16.3447C14.4557 16.4259 14.5013 16.5359 14.5013 16.6507L14.5113 18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM29.6553 17.7073C29.0019 15.6166 27.8201 13.7299 26.2241 12.2297C24.6281 10.7295 22.672 9.66648 20.545 9.14351C18.4179 8.62055 16.1919 8.65531 14.0822 9.24445C11.9726 9.83358 10.0506 10.9571 8.50226 12.5065C6.9539 14.0558 5.83155 15.9785 5.24375 18.0885C4.65595 20.1986 4.62259 22.4246 5.1469 24.5513C5.6712 26.678 6.73544 28.6334 8.23666 30.2285C9.73789 31.8235 11.6253 33.0042 13.7164 33.6562C16.1787 34.4343 18.821 34.4343 21.2834 33.6562C23.2547 33.0473 25.0477 31.9665 26.5066 30.5075C27.9655 29.0486 29.0464 27.2556 29.6553 25.2843C30.4333 22.822 30.4333 20.1796 29.6553 17.7173V17.7073ZM16.8056 27.3471C16.8056 27.5744 16.7608 27.7994 16.6738 28.0094C16.5868 28.2194 16.4594 28.4102 16.2986 28.5709C16.1379 28.7316 15.9471 28.8591 15.7372 28.9461C15.5272 29.0331 15.3021 29.0778 15.0748 29.0778H11.6536C11.1946 29.0778 10.7543 28.8955 10.4298 28.5709C10.1052 28.2463 9.92285 27.8061 9.92285 27.3471V23.9259C9.92285 23.6986 9.96761 23.4735 10.0546 23.2635C10.1416 23.0535 10.2691 22.8628 10.4298 22.702C10.5905 22.5413 10.7813 22.4138 10.9913 22.3269C11.2012 22.2399 11.4263 22.1951 11.6536 22.1951H15.0748C15.5338 22.1951 15.9741 22.3775 16.2986 22.702C16.6232 23.0266 16.8056 23.4668 16.8056 23.9259V27.3471ZM16.8056 19.0758C16.8056 19.303 16.7608 19.5281 16.6738 19.7381C16.5868 19.9481 16.4594 20.1389 16.2986 20.2996C16.1379 20.4603 15.9471 20.5878 15.7372 20.6747C15.5272 20.7617 15.3021 20.8065 15.0748 20.8065H11.6536C11.1946 20.8065 10.7543 20.6241 10.4298 20.2996C10.1052 19.975 9.92285 19.5348 9.92285 19.0758V15.6545C9.92285 15.1955 10.1052 14.7553 10.4298 14.4307C10.7543 14.1061 11.1946 13.9238 11.6536 13.9238H15.0748C15.5338 13.9238 15.9741 14.1061 16.2986 14.4307C16.6232 14.7553 16.8056 15.1955 16.8056 15.6545V19.0758ZM18.1942 22.6278C18.1967 22.5138 18.2432 22.4053 18.3238 22.3247C18.4043 22.2441 18.5129 22.1977 18.6269 22.1951H20.1061C20.2208 22.1951 20.3309 22.2407 20.412 22.3218C20.4932 22.403 20.5387 22.513 20.5387 22.6278V24.107C20.5387 24.2217 20.4932 24.3318 20.412 24.4129C20.3309 24.4941 20.2208 24.5397 20.1061 24.5397H18.6269C18.5121 24.5397 18.4021 24.4941 18.3209 24.4129C18.2398 24.3318 18.1942 24.2217 18.1942 24.107V22.6278ZM20.4884 28.6653C20.4884 28.78 20.4428 28.8901 20.3617 28.9712C20.2806 29.0524 20.1705 29.098 20.0557 29.098H18.6269C18.5129 29.0954 18.4043 29.049 18.3238 28.9684C18.2432 28.8878 18.1967 28.7792 18.1942 28.6653V27.2163C18.1942 27.1015 18.2398 26.9915 18.3209 26.9103C18.4021 26.8292 18.5121 26.7836 18.6269 26.7836H20.1061C20.2208 26.7836 20.3309 26.8292 20.412 26.9103C20.4932 26.9915 20.5387 27.1015 20.5387 27.2163L20.4884 28.6653ZM22.35 26.8037H20.9211C20.8064 26.8037 20.6963 26.7581 20.6152 26.677C20.534 26.5958 20.4884 26.4858 20.4884 26.371V24.922C20.491 24.8081 20.5374 24.6995 20.618 24.6189C20.6986 24.5383 20.8072 24.4919 20.9211 24.4894H22.35C22.4647 24.4894 22.5748 24.5349 22.6559 24.6161C22.7371 24.6972 22.7827 24.8073 22.7827 24.922V26.3509C22.7827 26.4657 22.7371 26.5757 22.6559 26.6569C22.5748 26.738 22.4647 26.7836 22.35 26.7836V26.8037ZM25.0769 28.6653C25.0743 28.7792 25.0279 28.8878 24.9473 28.9684C24.8667 29.049 24.7582 29.0954 24.6442 29.098H23.2154C23.1006 29.098 22.9905 29.0524 22.9094 28.9712C22.8283 28.8901 22.7827 28.78 22.7827 28.6653V27.2163C22.7827 27.1015 22.8283 26.9915 22.9094 26.9103C22.9905 26.8292 23.1006 26.7836 23.2154 26.7836H24.6442C24.759 26.7836 24.869 26.8292 24.9502 26.9103C25.0313 26.9915 25.0769 27.1015 25.0769 27.2163V28.6653ZM25.0769 24.0768C25.0769 24.1915 25.0313 24.3016 24.9502 24.3827C24.869 24.4639 24.759 24.5095 24.6442 24.5095H23.2154C23.1006 24.5095 22.9905 24.4639 22.9094 24.3827C22.8283 24.3016 22.7827 24.1915 22.7827 24.0768V22.6278C22.7827 22.513 22.8283 22.403 22.9094 22.3218C22.9905 22.2407 23.1006 22.1951 23.2154 22.1951H24.6442C24.7582 22.1977 24.8667 22.2441 24.9473 22.3247C25.0279 22.4053 25.0743 22.5138 25.0769 22.6278V24.0768ZM25.0769 19.0959C25.0769 19.3232 25.0321 19.5482 24.9452 19.7582C24.8582 19.9682 24.7307 20.159 24.57 20.3197C24.4093 20.4804 24.2185 20.6079 24.0085 20.6949C23.7985 20.7819 23.5734 20.8266 23.3462 20.8266H19.9249C19.6959 20.8266 19.4692 20.7812 19.2579 20.693C19.0466 20.6047 18.8549 20.4755 18.6939 20.3126C18.533 20.1498 18.4059 19.9566 18.3201 19.7443C18.2343 19.5319 18.1915 19.3047 18.1942 19.0758V15.6545C18.1942 15.1955 18.3765 14.7553 18.7011 14.4307C19.0257 14.1061 19.4659 13.9238 19.9249 13.9238H23.3462C23.5734 13.9238 23.7985 13.9685 24.0085 14.0555C24.2185 14.1425 24.4093 14.27 24.57 14.4307C24.7307 14.5914 24.8582 14.7822 24.9452 14.9922C25.0321 15.2022 25.0769 15.4272 25.0769 15.6545V19.0959ZM22.8732 15.2621H20.3979C20.2838 15.2607 20.1707 15.2822 20.0651 15.3252C19.9595 15.3682 19.8636 15.4319 19.7829 15.5125C19.7023 15.5932 19.6386 15.6891 19.5956 15.7947C19.5526 15.9003 19.5311 16.0134 19.5325 16.1275V18.6028C19.5311 18.7168 19.5526 18.83 19.5956 18.9356C19.6386 19.0412 19.7023 19.1371 19.7829 19.2177C19.8636 19.2984 19.9595 19.3621 20.0651 19.4051C20.1707 19.4481 20.2838 19.4695 20.3979 19.4682H22.8732C22.9872 19.4695 23.1004 19.4481 23.206 19.4051C23.3116 19.3621 23.4075 19.2984 23.4881 19.2177C23.5688 19.1371 23.6325 19.0412 23.6755 18.9356C23.7185 18.83 23.74 18.7168 23.7386 18.6028V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 15.2721H12.1265C12.0125 15.2708 11.8994 15.2923 11.7938 15.3353C11.6882 15.3783 11.5922 15.442 11.5116 15.5226C11.431 15.6032 11.3673 15.6992 11.3243 15.8048C11.2813 15.9104 11.2598 16.0235 11.2612 16.1375V18.6129C11.2598 18.7269 11.2813 18.84 11.3243 18.9456C11.3673 19.0512 11.431 19.1472 11.5116 19.2278C11.5922 19.3084 11.6882 19.3721 11.7938 19.4151C11.8994 19.4581 12.0125 19.4796 12.1265 19.4782H14.6019C14.7159 19.4796 14.829 19.4581 14.9346 19.4151C15.0402 19.3721 15.1362 19.3084 15.2168 19.2278C15.2974 19.1472 15.3611 19.0512 15.4041 18.9456C15.4471 18.84 15.4686 18.7269 15.4673 18.6129V16.1275C15.4686 16.0134 15.4471 15.9003 15.4041 15.7947C15.3611 15.6891 15.2974 15.5932 15.2168 15.5125C15.1362 15.4319 15.0402 15.3682 14.9346 15.3252C14.829 15.2822 14.7159 15.2607 14.6019 15.2621V15.2721ZM14.5113 18.0695C14.5088 18.1835 14.4624 18.292 14.3818 18.3726C14.3012 18.4532 14.1926 18.4996 14.0786 18.5022H12.6498C12.535 18.5022 12.425 18.4566 12.3438 18.3755C12.2627 18.2943 12.2171 18.1843 12.2171 18.0695V16.6507C12.2171 16.5359 12.2627 16.4259 12.3438 16.3447C12.425 16.2636 12.535 16.218 12.6498 16.218H14.0686C14.1833 16.218 14.2934 16.2636 14.3745 16.3447C14.4557 16.4259 14.5013 16.5359 14.5013 16.6507L14.5113 18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 15.252H12.1265C12.0125 15.2507 11.8994 15.2721 11.7938 15.3151C11.6882 15.3582 11.5922 15.4218 11.5116 15.5025C11.431 15.5831 11.3673 15.679 11.3243 15.7846C11.2813 15.8902 11.2598 16.0034 11.2612 16.1174V18.5928C11.2598 18.7068 11.2813 18.8199 11.3243 18.9255C11.3673 19.0311 11.431 19.127 11.5116 19.2077C11.5922 19.2883 11.6882 19.352 11.7938 19.395C11.8994 19.438 12.0125 19.4595 12.1265 19.4581H14.6019C14.7159 19.4595 14.829 19.438 14.9346 19.395C15.0402 19.352 15.1362 19.2883 15.2168 19.2077C15.2974 19.127 15.3611 19.0311 15.4041 18.9255C15.4471 18.8199 15.4686 18.7068 15.4673 18.5928V16.1275C15.4686 16.0134 15.4471 15.9003 15.4041 15.7947C15.3611 15.6891 15.2974 15.5932 15.2168 15.5125C15.1362 15.4319 15.0402 15.3682 14.9346 15.3252C14.829 15.2822 14.7159 15.2607 14.6019 15.2621V15.252ZM14.5113 18.0695C14.5088 18.1835 14.4624 18.292 14.3818 18.3726C14.3012 18.4532 14.1926 18.4996 14.0786 18.5022H12.6498C12.535 18.5022 12.425 18.4566 12.3438 18.3755C12.2627 18.2943 12.2171 18.1843 12.2171 18.0695V16.6507C12.2171 16.5359 12.2627 16.4259 12.3438 16.3447C12.425 16.2636 12.535 16.218 12.6498 16.218H14.0686C14.1833 16.218 14.2934 16.2636 14.3745 16.3447C14.4557 16.4259 14.5013 16.5359 14.5013 16.6507L14.5113 18.0695ZM14.6019 23.5234H12.1265C12.0125 23.522 11.8994 23.5435 11.7938 23.5865C11.6882 23.6295 11.5922 23.6932 11.5116 23.7738C11.431 23.8544 11.3673 23.9504 11.3243 24.056C11.2813 24.1616 11.2598 24.2747 11.2612 24.3887V26.8641C11.2598 26.9781 11.2813 27.0912 11.3243 27.1968C11.3673 27.3024 11.431 27.3984 11.5116 27.479C11.5922 27.5596 11.6882 27.6233 11.7938 27.6663C11.8994 27.7094 12.0125 27.7308 12.1265 27.7295H14.6019C14.7159 27.7308 14.829 27.7094 14.9346 27.6663C15.0402 27.6233 15.1362 27.5596 15.2168 27.479C15.2974 27.3984 15.3611 27.3024 15.4041 27.1968C15.4471 27.0912 15.4686 26.9781 15.4673 26.8641V24.3988C15.4686 24.2848 15.4471 24.1716 15.4041 24.066C15.3611 23.9604 15.2974 23.8645 15.2168 23.7839C15.1362 23.7032 15.0402 23.6396 14.9346 23.5965C14.829 23.5535 14.7159 23.5321 14.6019 23.5334V23.5234ZM14.5113 26.3408C14.5113 26.4556 14.4657 26.5657 14.3846 26.6468C14.3035 26.7279 14.1934 26.7735 14.0786 26.7735H12.6498C12.535 26.7735 12.425 26.7279 12.3438 26.6468C12.2627 26.5657 12.2171 26.4556 12.2171 26.3408V24.922C12.2171 24.8073 12.2627 24.6972 12.3438 24.6161C12.425 24.5349 12.535 24.4894 12.6498 24.4894H14.0686C14.1825 24.4919 14.2911 24.5383 14.3717 24.6189C14.4523 24.6995 14.4987 24.8081 14.5013 24.922L14.5113 26.3408ZM22.8732 15.2721H20.3979C20.2838 15.2708 20.1707 15.2923 20.0651 15.3353C19.9595 15.3783 19.8636 15.442 19.7829 15.5226C19.7023 15.6032 19.6386 15.6992 19.5956 15.8048C19.5526 15.9104 19.5311 16.0235 19.5325 16.1375V18.6129C19.5311 18.7269 19.5526 18.84 19.5956 18.9456C19.6386 19.0512 19.7023 19.1472 19.7829 19.2278C19.8636 19.3084 19.9595 19.3721 20.0651 19.4151C20.1707 19.4581 20.2838 19.4796 20.3979 19.4782H22.8732C22.9872 19.4796 23.1004 19.4581 23.206 19.4151C23.3116 19.3721 23.4075 19.3084 23.4881 19.2278C23.5688 19.1472 23.6325 19.0512 23.6755 18.9456C23.7185 18.84 23.74 18.7269 23.7386 18.6129V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.2721ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM14.6019 15.252H12.1265C12.0125 15.2507 11.8994 15.2721 11.7938 15.3151C11.6882 15.3582 11.5922 15.4218 11.5116 15.5025C11.431 15.5831 11.3673 15.679 11.3243 15.7846C11.2813 15.8902 11.2598 16.0034 11.2612 16.1174V18.5928C11.2598 18.7068 11.2813 18.8199 11.3243 18.9255C11.3673 19.0311 11.431 19.127 11.5116 19.2077C11.5922 19.2883 11.6882 19.352 11.7938 19.395C11.8994 19.438 12.0125 19.4595 12.1265 19.4581H14.6019C14.7159 19.4595 14.829 19.438 14.9346 19.395C15.0402 19.352 15.1362 19.2883 15.2168 19.2077C15.2974 19.127 15.3611 19.0311 15.4041 18.9255C15.4471 18.8199 15.4686 18.7068 15.4673 18.5928V16.1275C15.4686 16.0134 15.4471 15.9003 15.4041 15.7947C15.3611 15.6891 15.2974 15.5932 15.2168 15.5125C15.1362 15.4319 15.0402 15.3682 14.9346 15.3252C14.829 15.2822 14.7159 15.2607 14.6019 15.2621V15.252ZM14.5113 18.0695C14.5088 18.1835 14.4624 18.292 14.3818 18.3726C14.3012 18.4532 14.1926 18.4996 14.0786 18.5022H12.6498C12.535 18.5022 12.425 18.4566 12.3438 18.3755C12.2627 18.2943 12.2171 18.1843 12.2171 18.0695V16.6507C12.2171 16.5359 12.2627 16.4259 12.3438 16.3447C12.425 16.2636 12.535 16.218 12.6498 16.218H14.0686C14.1833 16.218 14.2934 16.2636 14.3745 16.3447C14.4557 16.4259 14.5013 16.5359 14.5013 16.6507L14.5113 18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695ZM22.8732 15.252H20.3979C20.2838 15.2507 20.1707 15.2721 20.0651 15.3151C19.9595 15.3582 19.8636 15.4218 19.7829 15.5025C19.7023 15.5831 19.6386 15.679 19.5956 15.7846C19.5526 15.8902 19.5311 16.0034 19.5325 16.1174V18.5928C19.5311 18.7068 19.5526 18.8199 19.5956 18.9255C19.6386 19.0311 19.7023 19.127 19.7829 19.2077C19.8636 19.2883 19.9595 19.352 20.0651 19.395C20.1707 19.438 20.2838 19.4595 20.3979 19.4581H22.8732C22.9872 19.4595 23.1004 19.438 23.206 19.395C23.3116 19.352 23.4075 19.2883 23.4881 19.2077C23.5688 19.127 23.6325 19.0311 23.6755 18.9255C23.7185 18.8199 23.74 18.7068 23.7386 18.5928V16.1275C23.74 16.0134 23.7185 15.9003 23.6755 15.7947C23.6325 15.6891 23.5688 15.5932 23.4881 15.5125C23.4075 15.4319 23.3116 15.3682 23.206 15.3252C23.1004 15.2822 22.9872 15.2607 22.8732 15.2621V15.252ZM22.7827 18.0695C22.7827 18.1843 22.7371 18.2943 22.6559 18.3755C22.5748 18.4566 22.4647 18.5022 22.35 18.5022H20.9211C20.8072 18.4996 20.6986 18.4532 20.618 18.3726C20.5374 18.292 20.491 18.1835 20.4884 18.0695V16.6507C20.4884 16.5359 20.534 16.4259 20.6152 16.3447C20.6963 16.2636 20.8064 16.218 20.9211 16.218H22.35C22.4647 16.218 22.5748 16.2636 22.6559 16.3447C22.7371 16.4259 22.7827 16.5359 22.7827 16.6507V18.0695Z",
                                fill: "url(#paint0_linear_2553_129075)"
                            }), t.jsx("path", {
                                d: "M17.5 8.76093C20.0196 8.76093 22.4825 9.50806 24.5775 10.9079C26.6724 12.3076 28.3052 14.2972 29.2694 16.625C30.2336 18.9527 30.4858 21.5141 29.9943 23.9853C29.5028 26.4564 28.2895 28.7263 26.5079 30.5079C24.7263 32.2895 22.4564 33.5028 19.9853 33.9943C17.5141 34.4858 14.9527 34.2336 12.625 33.2694C10.2972 32.3052 8.30764 30.6724 6.90786 28.5774C5.50807 26.4825 4.76094 24.0196 4.76094 21.5C4.76094 18.1214 6.10308 14.8812 8.49212 12.4921C10.8812 10.1031 14.1214 8.76093 17.5 8.76093ZM17.5 7C14.6322 7 11.8288 7.85041 9.44424 9.44369C7.05973 11.037 5.20122 13.3016 4.10375 15.9511C3.00628 18.6006 2.71913 21.5161 3.27862 24.3288C3.83811 27.1415 5.2191 29.7252 7.24696 31.753C9.27482 33.7809 11.8585 35.1619 14.6712 35.7214C17.4839 36.2809 20.3994 35.9937 23.0489 34.8963C25.6984 33.7988 27.963 31.9403 29.5563 29.5558C31.1496 27.1713 32 24.3678 32 21.5C31.9973 17.6552 30.4688 13.9686 27.7501 11.2499C25.0314 8.5312 21.3448 7.00267 17.5 7V7Z",
                                fill: "url(#paint1_linear_2553_129075)"
                            })]
                        }), t.jsx("rect", {
                            x: "32",
                            y: "4",
                            width: "2",
                            height: "8",
                            fill: "#08CE51"
                        }), t.jsx("rect", {
                            x: "29",
                            y: "9",
                            width: "2",
                            height: "8",
                            transform: "rotate(-90 29 9)",
                            fill: "#08CE51"
                        })]
                    }), t.jsxs("defs", {
                        children: [t.jsxs("linearGradient", {
                            id: "paint0_linear_2553_129075",
                            x1: "24.8253",
                            y1: "38.778",
                            x2: "8.60466",
                            y2: "0.510519",
                            gradientUnits: "userSpaceOnUse",
                            children: [t.jsx("stop", {
                                offset: "0.08",
                                stopColor: "#F7931E"
                            }), t.jsx("stop", {
                                offset: "0.79",
                                stopColor: "#FCEE21"
                            })]
                        }), t.jsxs("linearGradient", {
                            id: "paint1_linear_2553_129075",
                            x1: "3.644",
                            y1: "25.7866",
                            x2: "31.356",
                            y2: "17.2134",
                            gradientUnits: "userSpaceOnUse",
                            children: [t.jsx("stop", {
                                stopColor: "#F7931E"
                            }), t.jsx("stop", {
                                offset: "1",
                                stopColor: "#FCEE21"
                            })]
                        })]
                    })]
                })
            }), t.jsx("div", {
                style: {
                    display: "inline-flex",
                    flex: "auto"
                },
                children: C("label.bannerPromoteQRWallet")
            }), t.jsx("div", {
                style: {
                    display: "inline-flex"
                },
                children: t.jsx(n1, {
                    className: "zaui-color-b70",
                    icon: "zi-chevron-right",
                    size: 16
                })
            })]
        })
    };
var N2;
const g3 = V.div(N2 || (N2 = k(["\n  display: flex;\n  align-items: center;\n  border-radius: 8px;\n  background-color: #f0fbff;\n  padding: 8px 16px;\n  font-size: 13px;\n"]))),
    Q1 = (e, n = ",") => {
        const i = String(e);
        return i.length > 3 ? i.replace(/\B(?=(\d{3})+(?!\d))/g, n) : i
    },
    N3 = e => {
        const n = /^\d*$/g,
            i = e.trim();
        if (!n.test(i)) return i;
        if (i.length === 10) return i.replace(/(\d{4})(\d{3})(\d{3})/, "$1 $2 $3");
        const C = [],
            r = i.length % 4;
        let a = 0,
            s = r;
        for (; a < i.length;) {
            const l = s > 0 || r === 0 ? 4 : 3;
            C.push(i.substring(a, a + l)), a += l, s -= 1
        }
        return C.join(" ")
    },
    k3 = e => {
        const n = /^\d*$/g,
            i = e.trim();
        if (!n.test(i)) return i;
        if (i.length === 10) return i.replace(/(\d{4})(\d{3})(\d{3})/, "$1 $2 $3");
        const C = [],
            r = i.length % 4;
        let a = 0,
            s = r;
        for (; a < i.length;) {
            const l = s > 0 || r === 0 ? 4 : 3;
            C.push(i.substring(a, a + l)), a += l, s -= 1
        }
        return C.join(" ")
    },
    V3 = e => e.charAt(0).toUpperCase() + e.slice(1).toLowerCase(),
    E1 = e => {
        const {
            avatar: n,
            title: i,
            actions: C,
            onCopy: r
        } = e, a = d1(), {
            t: s
        } = j(), l = p.useCallback(c => {
            var d;
            if (c.copy) {
                m5(c.copy);
                const g = /\(.*?\)/g,
                    I = ((d = c.label) == null ? void 0 : d.replace(g, "").replace(/\s{2,}/g, " ").trim()) || "";
                a.openSnackbar({
                    text: V3(s("message.copiedContent", {
                        content: I
                    })),
                    type: "success"
                }), K.clickBtnCopy({
                    label: c.key
                }), r == null || r(c)
            }
        }, [r, a, s]);
        return t.jsxs(A3, {
            children: [t.jsxs(f3, {
                children: [t.jsx(B3, {
                    children: n
                }), t.jsx(L, {
                    size: "large",
                    children: i
                })]
            }), t.jsx(e1, {
                children: C.map(c => t.jsxs(e1.Item, {
                    suffix: c.copy ? t.jsx(u, {
                        flex: !0,
                        alignItems: "center",
                        style: {
                            height: "100%"
                        },
                        children: t.jsx(U, {
                            variant: c.primaryCopy ? "primary" : "secondary",
                            onClick: () => {
                                l(c)
                            },
                            size: "small",
                            children: s("button.copy")
                        })
                    }) : null,
                    children: [c.title && t.jsx(L, {
                        size: "large",
                        bold: !0,
                        children: c.title
                    }), c.label && t.jsx(L, {
                        size: "small",
                        className: "zaui-text-02",
                        children: c.label
                    }), c.value && t.jsx(L, {
                        size: "large",
                        bold: c.bold,
                        children: c.value
                    })]
                }, c.key))
            })]
        })
    };
var k2;
const A3 = V.div(k2 || (k2 = k(["\n  border-radius: 12px;\n  border: 1px solid var(--zmp-border-01);\n  box-shadow: var(--zmp-shadow-01);\n  overflow: hidden;\n  overflow-wrap: anywhere;\n  word-break: break-word;\n"])));
var V2;
const f3 = V.div(V2 || (V2 = k(["\n  display: flex;\n  align-items: center;\n  background-color: var(--zmp-color-ng10);\n  padding: 16px;\n"])));
var A2;
const B3 = V.div(A2 || (A2 = k(["\n  display: flex;\n  flex: none;\n  align-items: center;\n  justify-content: center;\n  width: 40px;\n  height: 40px;\n  box-sizing: border-box;\n  border-radius: 8px;\n  background-color: white;\n  border: 0.5px solid var(--zmp-border-01);\n  margin-right: 16px;\n  overflow: hidden;\n"]))),
    x3 = ({
        data: e
    }) => {
        const {
            t: n
        } = j(), i = p.useMemo(() => {
            const C = [];
            return C.push({
                key: "accountName",
                label: n("label.accountName"),
                value: e.name.toUpperCase(),
                bold: !0
            }), e.phone && C.push({
                key: "phoneNumber",
                label: n("label.phoneNumber"),
                value: k3(e.phone),
                copy: e.phone,
                primaryCopy: !0
            }), e.content && C.push({
                key: "content",
                label: n("label.content"),
                value: e.content,
                copy: e.content
            }), Number(e.amount) && C.push({
                key: "amount",
                label: n("label.amount"),
                value: Q1(Number(e.amount), "."),
                copy: e.amount,
                bold: !0
            }), C
        }, [e.amount, e.content, e.name, e.phone, n]);
        return t.jsx(E1, {
            avatar: t.jsx(_5, {
                size: 40
            }),
            title: "MoMo",
            actions: i
        })
    },
    p1 = () => {
        const {
            t: e
        } = j();
        return t.jsx($, {
            color: "text-02",
            size: "xSmall",
            children: e("disclaimer.check_info")
        })
    };
var Y2 = (e => (e.PERSONAL = "MOMO_PERSONAL", e))(Y2 || {});
const S3 = () => {
        const [e] = m1(C => [C.qrContent]), n = p.useMemo(() => {
            if (!e) return null;
            const [C, , r, a, , , , s, l, c] = e.split("|");
            return {
                type: Y2.PERSONAL,
                version: C,
                phone: r,
                name: a,
                amount: s,
                content: l,
                code: c
            }
        }, [e]), i = p.useMemo(() => !((n == null ? void 0 : n.code) !== "transfer_myqr" || !n.name), [n]);
        return {
            data: n,
            isSupported: i
        }
    },
    H3 = () => {
        const {
            t: e
        } = j();
        h1(e("header.momo"));
        const {
            data: n,
            isSupported: i
        } = S3(), {
            openApp: C
        } = U2(), r = () => {
            K.clickOpenMomoApp(), n && C({
                data: n
            })
        };
        return j1(() => {
            const a = {
                type: n == null ? void 0 : n.type,
                name: n != null && n.name ? 1 : 0,
                phone: n != null && n.phone ? 1 : 0,
                amount: n != null && n.amount ? 1 : 0,
                content: n != null && n.content ? 1 : 0
            };
            K.pageLoadDone(a)
        }, !!(i && n)), i ? t.jsxs(X, {
            children: [t.jsxs(r1, {
                children: [t.jsx(u, {
                    children: t.jsx(u, {
                        children: n && t.jsx(x3, {
                            data: n
                        })
                    })
                }), t.jsx(u, {
                    mb: 6
                }), t.jsx(p1, {}), t.jsx(u, {
                    mb: 6
                }), t.jsx(u, {
                    children: t.jsx(X2, {
                        src: "home",
                        type: n == null ? void 0 : n.type
                    })
                })]
            }), t.jsx(M5, {
                children: t.jsx(U, {
                    fullWidth: !0,
                    onClick: r,
                    children: e("button.openMomoApp")
                })
            })]
        }) : t.jsx(X, {
            children: t.jsx(D2, {})
        })
    },
    L1 = ({
        data: e,
        bankAccountName: n
    }) => {
        var r, a;
        const {
            t: i
        } = j(), C = p.useMemo(() => {
            const s = [];
            return n && s.push({
                key: "accountName",
                label: i("label.accountName"),
                value: n.toUpperCase()
            }), e.bankNumber && s.push({
                key: "accountNumber",
                label: i("label.accountNumber"),
                value: N3(e.bankNumber),
                copy: e.bankNumber,
                primaryCopy: !0
            }), e.content && s.push({
                key: "content",
                label: i("label.content"),
                value: e.content,
                copy: e.content
            }), e.amount && s.push({
                key: "amount",
                label: i("label.amount"),
                value: Q1(Number(String(e.amount).trim().replace(/((?![\d.]).)/gm, "")), "."),
                copy: e.amount,
                bold: !0
            }), s
        }, [n, e.amount, e.bankNumber, e.content, i]);
        return t.jsx(E1, {
            avatar: t.jsx(B1, {
                size: 36,
                app: ((r = e.bank) == null ? void 0 : r.key) || ""
            }),
            title: ((a = e.bank) == null ? void 0 : a.shortName) || "",
            actions: C
        })
    };
class I3 {
    constructor(n = {}) {
        U1(this, "map");
        this.map = new Map(Object.entries(n))
    }
    append(n, i) {
        this.map.set(n, i)
    }
    delete(n) {
        this.map.delete(n)
    }
    toString() {
        return Array.from(this.map).filter(([, n]) => n != null).map(([n, i]) => typeof i == "object" ? "".concat(n, "=").concat(encodeURIComponent(JSON.stringify(i))) : "".concat(n, "=").concat(encodeURIComponent(i))).join("&")
    }
    get[Symbol.toStringTag]() {
        return this.toString()
    }
}
const y3 = "00020101021238530010A0000007270123000697041601092576788590208QRIBFTTA53037045405100005802VN62150811Chuyen tien630453E6",
    M3 = () => {
        h1("Napas Deeplink");
        const [e, n] = p.useState(""), [i, C] = p.useState(""), [r, a] = p.useState(!1), s = P1(), l = d1(), c = p.useMemo(() => {
            const m = new A.QRPay(e != null ? e : "");
            return m.provider.name !== A.QRProvider.VIETQR ? null : m
        }, [e]), d = p.useMemo(() => {
            var b, B, S, M, H, P, Q;
            return !c || !(c != null && c.isValid) ? null : {
                type: (b = c == null ? void 0 : c.provider) == null ? void 0 : b.name,
                service: (B = c == null ? void 0 : c.provider) == null ? void 0 : B.service,
                bank: T1((S = c.consumer) == null ? void 0 : S.bankBin),
                bankNumber: (M = c.consumer) == null ? void 0 : M.bankNumber,
                amount: c == null ? void 0 : c.amount,
                content: (H = c.additionalData) == null ? void 0 : H.purpose,
                store: (P = c.additionalData) == null ? void 0 : P.store,
                terminal: (Q = c.additionalData) == null ? void 0 : Q.terminal
            }
        }, [c]), g = p.useMemo(() => {
            if (!c) return "";
            const m = new I3,
                b = (B, S) => {
                    if (!S) return;
                    const M = S.split(".").reduce((H, P) => H[P], c);
                    M && m.append(B, M)
                };
            return b("tc", "currency"), b("cc", "nation"), b("mc", "category"), b("pn", "merchant.name"), b("pa", "city"), b("an", "consumer.bankNumber"), b("bank", "consumer.bankBin"), b("am", "amount"), b("bn", "additionalData.billNumber"), b("mm", "additionalData.mobileNumber"), b("sl", "additionalData.store"), b("lm", "additionalData.loyaltyNumber"), b("rl", "additionalData.reference"), b("cl", "additionalData.customerLabel"), b("tl", "additionalData.terminal"), b("tn", "additionalData.purpose"), "".concat(c.provider.service, "?").concat(m.toString())
        }, [c]), I = () => {
            T.openQR(m => {
                var b;
                m.error_code === 0 ? n((b = m.data.content) != null ? b : "") : console.log(m)
            })
        }, y = () => {
            const m = "".concat(i, "://").concat(g);
            s(() => {
                a(!0), T.openOutApp(m, () => {})
            }).catch(() => {
                l.openSnackbar({
                    text: "KhÃ´ng thá»ƒ má»Ÿ á»©ng dá»¥ng! HÃ£y Ä‘áº£m báº£o á»©ng dá»¥ng Ä‘Ã£ Ä‘Æ°á»£c cÃ i Ä‘áº·t trÃªn thiáº¿t bá»‹ cá»§a báº¡n.",
                    type: "warning",
                    duration: 3e3
                })
            }).finally(() => {
                a(!1)
            })
        };
        return t.jsx(X, {
            children: t.jsxs(r1, {
                style: {
                    justifyContent: e ? "flex-start" : "center"
                },
                children: [t.jsx(u, {
                    children: t.jsx(U, {
                        variant: "secondary",
                        fullWidth: !0,
                        onClick: I,
                        prefixIcon: t.jsx(n1, {
                            icon: "zi-qrline"
                        }),
                        children: "QuÃ©t mÃ£ QR"
                    })
                }), !e && t.jsx(u, {
                    mt: 2,
                    children: t.jsx(U, {
                        fullWidth: !0,
                        variant: "tertiary",
                        onClick: () => n(y3),
                        children: "DÃ¹ng mÃ£ QR Demo"
                    })
                }), c && t.jsx("div", {
                    children: d && (c == null ? void 0 : c.provider.guid) === "A000000727" && t.jsxs(u, {
                        mb: 4,
                        children: [t.jsx(u, {
                            mt: 4
                        }), t.jsx(L1, {
                            data: d
                        }), t.jsx(u, {
                            mb: 6
                        }), t.jsx(u, {
                            children: t.jsx(o1, {
                                size: "small",
                                style: {
                                    whiteSpace: "pre-wrap"
                                },
                                children: "Má»Ÿ á»©ng dá»¥ng ngÃ¢n hÃ ng"
                            })
                        }), t.jsx(u, {
                            mb: 4
                        }), t.jsx(u, {
                            children: t.jsx(K1, {
                                value: i,
                                onChange: m => C(m.target.value),
                                label: "Scheme cá»§a app NgÃ¢n hÃ ng",
                                placeholder: "bank_app_name",
                                autoCapitalize: "off"
                            })
                        }), t.jsx(u, {
                            mb: 2
                        }), t.jsx("div", {
                            children: t.jsx($, {
                                children: "Deeplink"
                            })
                        }), t.jsxs("pre", {
                            style: {
                                wordBreak: "break-all",
                                display: "block",
                                whiteSpace: "break-spaces"
                            },
                            children: [i || t.jsx("i", {
                                children: "bank_app_name"
                            }), "://", g]
                        }), t.jsx(u, {
                            mb: 4
                        }), t.jsx(U, {
                            fullWidth: !0,
                            disabled: !i,
                            onClick: y,
                            children: "Má»Ÿ Deeplink"
                        })]
                    })
                }), t.jsx(f1, {
                    visible: r,
                    text: "Äang má»Ÿ..."
                })]
            })
        })
    };
var f2;
const v1 = V.div(f2 || (f2 = k(["\n  position: relative;\n  display: flex;\n  flex-direction: column;\n  justify-content: center;\n  align-items: center;\n  padding: 8px;\n  cursor: pointer;\n  color: var(--zmp-text-color);\n  font-size: 10px;\n  line-height: 14px;\n  border: 1px solid ", ";\n  border-radius: 8px;\n  width: 104px;\n\n  &:active {\n    background-color: var(--zmp-pressed-bg-color);\n  }\n\n  & .app-name {\n    text-align: center;\n    overflow-wrap: anywhere;\n    display: -webkit-box;\n    word-break: break-word;\n    overflow: hidden;\n    text-overflow: ellipsis;\n    -webkit-line-clamp: 2;\n    -webkit-box-orient: vertical;\n  }\n"])), e => e.bold ? "var(--zmp-border-01)" : "var(--zmp-color-ng20)");
var B2;
const J2 = V.div(B2 || (B2 = k(["\n  display: flex;\n  flex-direction: row;\n  overflow-x: auto;\n  overflow-y: hidden;\n  padding: 24px ", "px 0px;\n  margin: -24px -", "px 0px;\n\n  -webkit-overflow-scrolling: touch;\n  -ms-overflow-style: none;\n  scrollbar-width: none;\n  &::-webkit-scrollbar {\n    display: none;\n    width: 0 !important;\n    height: 0 !important;\n    -webkit-appearance: none;\n    background: transparent;\n  }\n\n  & > * {\n    flex-shrink: 0;\n    &:not(:last-of-type) {\n      margin-right: 8px;\n    }\n  }\n"])), e => e.offset || 0, e => e.offset || 0),
    e5 = ({
        data: e
    }) => {
        const {
            t: n
        } = j(), i = p.useMemo(() => {
            var r, a;
            const C = [];
            return e.store && C.push({
                key: "store",
                title: (r = e.store) != null ? r : "",
                value: (a = e.terminal) != null ? a : ""
            }), e.content && C.push({
                key: "content",
                label: n("label.content"),
                value: e.content,
                copy: e.content
            }), e.amount && C.push({
                key: "amount",
                label: n("label.amount"),
                value: Q1(Number(e.amount), "."),
                copy: e.amount,
                bold: !0
            }), C
        }, [e, n]);
        return t.jsx(E1, {
            avatar: t.jsx(w5, {
                size: 32
            }),
            title: "VNPAY",
            actions: i
        })
    },
    v3 = {
        [o.ABBANK]: {
            bank: o.ABBANK,
            scheme: "abbankmobile",
            packageId: "com.vnpay.abbank",
            appStoreId: "id1137160023",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.ACB]: {
            bank: o.ACB,
            scheme: "acbapp",
            packageId: "mobile.acb.com.vn",
            appStoreId: "id950141024",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.AGRIBANK]: {
            bank: o.AGRIBANK,
            scheme: "agribankmobile",
            packageId: "com.vnpay.Agribank3g",
            appStoreId: "id935944952",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.BAC_A_BANK]: {
            bank: o.BAC_A_BANK,
            packageId: "com.bab.retailUAT",
            appStoreId: "id1441408786",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.BAOVIET_BANK]: {
            bank: o.BAOVIET_BANK,
            scheme: "baovietmobile",
            packageId: "com.vnpay.bvbank",
            appStoreId: "id1504422967",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.BIDC]: {
            bank: o.BIDC,
            scheme: "bidcvnmobile",
            packageId: "com.vnpay.bidc",
            appStoreId: "id1043501726",
            supportVietQR: !1,
            supportVNPayQR: !0
        },
        [o.BIDV]: {
            bank: o.BIDV,
            scheme: "bidvsmartbanking",
            packageId: "com.vnpay.bidv",
            appStoreId: "id1061867449",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.CAKE]: {
            bank: o.CAKE,
            scheme: "cake.vn",
            packageId: "xyz.be.cake",
            appStoreId: "id1551907051",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.CBBANK]: {
            bank: o.CBBANK,
            packageId: "cbbank.vn.mobile",
            appStoreId: "id1531443181",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.CIMB]: {
            bank: o.CIMB,
            scheme: "cimb",
            packageId: "vn.cimbbank.octo",
            appStoreId: "id1318127958",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.COOP_BANK]: {
            bank: o.COOP_BANK,
            scheme: "coopbankmobile",
            packageId: "com.vnpay.coopbank",
            appStoreId: "id1578445811",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.DBS_BANK]: {
            bank: o.DBS_BANK,
            packageId: "com.dbs.sg.dbsmbanking",
            appStoreId: "id1068403826",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.DONG_A_BANK]: {
            bank: o.DONG_A_BANK,
            packageId: "com.dongabank.mobilenternet",
            appStoreId: "id993124125",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.EXIMBANK]: {
            bank: o.EXIMBANK,
            scheme: "com.vnpay.eximbankomnimobile",
            schemeAndroid: "eximbankomnimobile",
            packageId: "com.vnpay.EximBankOmni",
            appStoreId: "id1571427361",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.GPBANK]: {
            bank: o.GPBANK,
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.HDBANK]: {
            bank: o.HDBANK,
            scheme: "hdbankmobile",
            packageId: "com.vnpay.hdbank",
            appStoreId: "id1461658565",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.HONGLEONG_BANK]: {
            bank: o.HONGLEONG_BANK,
            packageId: "my.com.hongleongconnect.mobileconnect",
            appStoreId: "id1446719260",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.HSBC]: {
            bank: o.HSBC,
            packageId: "vn.hsbc.hsbcvietnam",
            appStoreId: "id1472163155",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.IBK_HN]: {
            bank: o.IBK_HN,
            scheme: "ionebankglobal",
            packageId: "com.ibk.neobanking.mini",
            appStoreId: "id787064809",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.IBK_HCM]: {
            bank: o.IBK_HCM,
            scheme: "ionebankglobal",
            packageId: "com.ibk.neobanking.mini",
            appStoreId: "id787064809",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.INDOVINA_BANK]: {
            bank: o.INDOVINA_BANK,
            scheme: "ivbmobilebanking",
            packageId: "com.vnpay.ivb",
            appStoreId: "id1096963960",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.KASIKORN_BANK]: {
            bank: o.KASIKORN_BANK,
            scheme: "kbank.kplusvn",
            packageId: "com.kasikornbank.kplus.vn",
            appStoreId: "id1586576195",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.KIENLONG_BANK]: {
            bank: o.KIENLONG_BANK,
            scheme: "kienlongbankmobilebanking",
            packageId: "com.sunshine.ksbank",
            appStoreId: "id1562823941",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.KOOKMIN_BANK_HN]: {
            bank: o.KOOKMIN_BANK_HN,
            packageId: "com.kbstar.global",
            appStoreId: "id1542727700",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.KOOKMIN_BANK_HCM]: {
            bank: o.KOOKMIN_BANK_HCM,
            packageId: "com.kbstar.global",
            appStoreId: "id1542727700",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.LIENVIETPOST_BANK]: {
            bank: o.LIENVIETPOST_BANK,
            scheme: "lv24h",
            packageId: "vn.com.lpb.lienviet24h",
            appStoreId: "id1488794748",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.MBBANK]: {
            bank: o.MBBANK,
            scheme: "mbmobile",
            packageId: "com.mbmobile",
            appStoreId: "id1205807363",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.MSB]: {
            bank: o.MSB,
            scheme: "msbmobile",
            packageId: "vn.com.msb.smartBanking",
            appStoreId: "id436134873",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.NAM_A_BANK]: {
            bank: o.NAM_A_BANK,
            scheme: "nabTransferMoney",
            packageId: "ops.namabank.com.vn",
            appStoreId: "id1456997296",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.NCB]: {
            bank: o.NCB,
            scheme: "ncbizimobile",
            packageId: "com.ncb.bank",
            appStoreId: "id1465217154",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.NONGHYUP_BANK_HN]: {
            bank: o.NONGHYUP_BANK_HN,
            scheme: "newnhsmartbanking",
            packageId: "nh.smart.banking",
            appStoreId: "id1444712671",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.OCB]: {
            bank: o.OCB,
            scheme: "omniapp",
            packageId: "com.ocb.omniextra",
            appStoreId: "id1358682577",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.OCEANBANK]: {
            bank: o.OCEANBANK,
            scheme: "oceanbankmobilebanking",
            packageId: "com.vnpay.ocean",
            appStoreId: "id1469028843",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.PGBANK]: {
            bank: o.PGBANK,
            packageId: "pgbankApp.pgbank.com.vn",
            appStoreId: "id1537765475",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.PUBLIC_BANK]: {
            bank: o.PUBLIC_BANK,
            scheme: "publicbankmobile",
            packageId: "com.vnpay.publicbank",
            appStoreId: "id1573736472",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.PVCOM_BANK]: {
            bank: o.PVCOM_BANK,
            scheme: "pvcombankapp",
            packageId: "com.vsii.pvcombank",
            appStoreId: "id957284067",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.SACOMBANK]: {
            bank: o.SACOMBANK,
            scheme: "sacombankmobile",
            packageId: "src.com.sacombank",
            appStoreId: "id885814869",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.SAIGONBANK]: {
            bank: o.SAIGONBANK,
            scheme: "Sgbmobile",
            packageId: "com.vnpay.sgbank",
            appStoreId: "id1481832587",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.SCB]: {
            bank: o.SCB,
            scheme: "scbmobilebanking",
            packageId: "com.vnpay.SCB",
            appStoreId: "id954973621",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.SEA_BANK]: {
            bank: o.SEA_BANK,
            scheme: "seabankmobile",
            packageId: "vn.com.seabank.mb1",
            appStoreId: "id846407152",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.SHB]: {
            bank: o.SHB,
            scheme: "shbmobile",
            packageId: "vn.shb.mbanking",
            appStoreId: "id538278798",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.SHINHAN_BANK]: {
            bank: o.SHINHAN_BANK,
            scheme: "shinhanglbvnbank",
            packageId: "com.shinhan.global.vn.bank",
            appStoreId: "id1071033810",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.STANDARD_CHARTERED_BANK]: {
            bank: o.STANDARD_CHARTERED_BANK,
            packageId: "com.sc.mobilebanking.vn",
            appStoreId: "id1146741999",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.TECHCOMBANK]: {
            bank: o.TECHCOMBANK,
            scheme: "tcb",
            packageId: "vn.com.techcombank.bb.app",
            appStoreId: "id1548623362",
            supportVietQR: !0,
            supportVNPayQR: !0,
            supportSignedDeeplink: !0
        },
        [o.TIMO]: {
            bank: o.TIMO,
            scheme: "plus",
            packageId: "io.lifestyle.plus",
            appStoreId: "id1521230347",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.TPBANK]: {
            bank: o.TPBANK,
            scheme: "hydro",
            packageId: "com.tpb.mb.gprsandroid",
            appStoreId: "id450464147",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.UBANK]: {
            bank: o.UBANK,
            packageId: "vn.vpbank.ubank",
            appStoreId: "id1529056628",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.UNITED_OVERSEAS_BANK]: {
            bank: o.UNITED_OVERSEAS_BANK,
            scheme: "mightyapp",
            packageId: "com.uob.mightyvn",
            appStoreId: "id1174327324",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.VIB]: {
            bank: o.VIB,
            scheme: "myvib2",
            packageId: "com.vib.myvib2",
            appStoreId: "id1626624790",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.VIET_A_BANK]: {
            bank: o.VIET_A_BANK,
            scheme: "vabmobilebanking",
            packageId: "phn.com.vn.mb",
            appStoreId: "id910897337",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.VIET_BANK]: {
            bank: o.VIET_BANK,
            scheme: "vietbankmobilebanking",
            packageId: "com.vnpay.vietbank",
            appStoreId: "id1461658565",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.VIETCAPITAL_BANK]: {
            bank: o.VIETCAPITAL_BANK,
            packageId: "vn.banvietbank.mobilebanking",
            appStoreId: "id1526444697",
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.VIETCOMBANK]: {
            bank: o.VIETCOMBANK,
            scheme: "vietcombankmobile",
            packageId: "com.VCB",
            appStoreId: "id561433133",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.VIETINBANK]: {
            bank: o.VIETINBANK,
            scheme: "vietinbankmobile",
            packageId: "com.vietinbank.ipay",
            appStoreId: "id689963454",
            supportVietQR: !0,
            supportVNPayQR: !0
        },
        [o.VPBANK]: {
            bank: o.VPBANK,
            scheme: "vpbankneo",
            packageId: "com.vnpay.vpbankonline",
            appStoreId: "id1209349510",
            supportVietQR: !0,
            supportVNPayQR: !1
        },
        [o.VRB]: {
            bank: o.VRB,
            supportVietQR: !1,
            supportVNPayQR: !1
        },
        [o.WOORI_BANK]: {
            bank: o.WOORI_BANK,
            scheme: "wvbs",
            packageId: "vn.com.woori.smart",
            appStoreId: "id1501785125",
            supportVietQR: !0,
            supportVNPayQR: !1
        }
    },
    _3 = Object.values(v3),
    n5 = _3.map(e => {
        const n = {
            ...e
        };
        switch (e.bank) {
            case A.BankKey.EXIMBANK:
                n.scheme = Y() ? n.scheme : n.schemeAndroid;
                break
        }
        return {
            ...n,
            ...h3[e.bank],
            type: "bank",
            key: e.bank
        }
    }),
    t5 = [...n5.filter(e => e.supportVietQR && e.scheme), a1],
    z = t5.reduce((e, n) => (e[n.key] = {
        ...n,
        type: n.type || "bank"
    }, e), {}),
    K3 = [z.techcombank, a1, z.namabank, z.vietcombank, z.mbbank, z.vietinbank],
    o5 = n5.filter(e => e.supportVNPayQR && e.scheme),
    J = o5.reduce((e, n) => (e[n.bank] = {
        ...n,
        type: "bank"
    }, e), {}),
    w3 = [J.techcombank, J.namabank, J.vietcombank, J.vietinbank, J.bidv, J.agribank],
    Z1 = [z.techcombank, z.namabank],
    k1 = String(Date.now()),
    y1 = "00020101021238530010A0000007270123000697041601092576788590208QRIBFTTA53037045405100005802VN62150811Chuyen tien630453E6",
    R3 = "00020101021126280010A0000007750110010215477853037045802VN5912TUGIACOMPANY62310315TU GIA COMPUTER0708TUGIACO16304DF44",
    O3 = () => {
        const {
            t: e
        } = j();
        h1(e("header.home"));
        const n = d1(),
            [i, C] = p.useState(!1),
            [r, a] = p.useState(y1),
            s = P1(),
            l = p.useMemo(() => {
                const f = new A.QRPay(r != null ? r : "");
                return f.provider.guid === "908405" && (f.provider.name = A.QRProvider.VNPAY), f
            }, [r]),
            c = p.useMemo(() => {
                var w, x, R, G, E, D, s1;
                return l.isValid ? {
                    type: (w = l == null ? void 0 : l.provider) == null ? void 0 : w.name,
                    service: (x = l == null ? void 0 : l.provider) == null ? void 0 : x.service,
                    bank: T1((R = l.consumer) == null ? void 0 : R.bankBin),
                    bankNumber: (G = l.consumer) == null ? void 0 : G.bankNumber,
                    amount: l == null ? void 0 : l.amount,
                    content: (E = l.additionalData) == null ? void 0 : E.purpose,
                    store: (D = l.additionalData) == null ? void 0 : D.store,
                    terminal: (s1 = l.additionalData) == null ? void 0 : s1.terminal
                } : null
            }, [l]),
            [d, g] = p.useState(A.QRProvider.VIETQR),
            I = "QRPay",
            y = "Zalo",
            m = "zalo://start",
            b = p.useMemo(() => ({
                qrContent: r || "",
                targetPage: I,
                source: y,
                timestamp: k1
            }), [r]),
            B = V1({
                queryKey: ["signData", b],
                queryFn: () => M1(A.BankKey.TECHCOMBANK, b)
            }),
            S = V1({
                queryKey: ["signData", {
                    ...b,
                    callbackurl: m
                }],
                queryFn: () => M1(A.BankKey.TECHCOMBANK, {
                    callbackurl: m,
                    ...b
                })
            }),
            M = B.data || "",
            H = S.data || "",
            P = f => {
                if (!B.isFetching) {
                    if (B.isError) {
                        n.openSnackbar({
                            text: "CÃ³ lá»—i khi kÃ½ dá»¯ liá»‡u",
                            type: "error"
                        }), console.log(B.error);
                        return
                    }
                    s(() => {
                        var w;
                        switch (C(!0), f.key) {
                            case A.BankKey.TECHCOMBANK:
                                G2({
                                    content: r || "",
                                    signature: H,
                                    callbackurl: m,
                                    timestamp: k1
                                });
                                break;
                            case A.BankKey.NAM_A_BANK:
                                $2({
                                    bankCode: ((w = c == null ? void 0 : c.bank) == null ? void 0 : w.bin) || "",
                                    accountNumber: (c == null ? void 0 : c.bankNumber) || "",
                                    amount: (c == null ? void 0 : c.amount) || "",
                                    description: (c == null ? void 0 : c.content) || ""
                                });
                                break;
                            case A.BankKey.BIDV:
                                W1({
                                    appScheme: "dl.bidvsmartbanking.vn",
                                    appHost: "applink",
                                    content: r || "",
                                    signature: M,
                                    timestamp: k1
                                });
                                break;
                            case A.BankKey.TPBANK:
                                W1({
                                    appScheme: "hydro",
                                    appHost: "applink",
                                    content: r || "",
                                    signature: M,
                                    timestamp: k1
                                });
                                break
                        }
                    }).catch(() => {
                        if (f != null && f.appStoreId && Y()) {
                            const w = "https://apps.apple.com/us/app/".concat(f.appStoreId);
                            T.openOutApp(w, x => {})
                        } else f.packageId && !Y() ? T.openOutApp("market://details?id=".concat(f.packageId), w => {}) : n.openSnackbar({
                            text: "KhÃ´ng thá»ƒ má»Ÿ á»©ng dá»¥ng!",
                            type: "warning",
                            duration: 3e3
                        })
                    }).finally(() => {
                        C(!1)
                    })
                }
            },
            Q = () => {
                T.openQR(f => {
                    f.error_code === 0 ? a(f.data.content || y1) : console.log(f)
                })
            };
        return p.useEffect(() => {
            c != null && c.type && g(c.type)
        }, [c == null ? void 0 : c.type]), t.jsx(X, {
            children: t.jsxs(r1, {
                children: [t.jsxs(x1, {
                    id: "tab",
                    className: "tab-center",
                    activeKey: d,
                    onChange: f => {
                        f === A.QRProvider.VIETQR ? a(y1) : a(R3)
                    },
                    children: [t.jsx(x1.Tab, {
                        label: "VietQR",
                        children: t.jsx(u, {
                            px: 1,
                            pt: 4,
                            children: (c == null ? void 0 : c.type) === A.QRProvider.VIETQR && t.jsxs(u, {
                                mb: 4,
                                children: [t.jsx(u, {
                                    mb: 4,
                                    children: t.jsx(o1, {
                                        size: "small",
                                        children: e("home.vietqr.step1.label")
                                    })
                                }), t.jsx(u, {
                                    children: t.jsx(L1, {
                                        data: c
                                    })
                                }), t.jsx(u, {
                                    mb: 6
                                }), t.jsx(p1, {}), t.jsx(u, {
                                    mb: 6
                                }), t.jsx(u, {
                                    children: t.jsx(o1, {
                                        size: "small",
                                        style: {
                                            whiteSpace: "pre-wrap"
                                        },
                                        children: e("home.vietqr.step2.label")
                                    })
                                })]
                            })
                        })
                    }, A.QRProvider.VIETQR), t.jsx(x1.Tab, {
                        label: "VNPayQR",
                        children: t.jsx(u, {
                            px: 1,
                            pt: 4,
                            children: (c == null ? void 0 : c.type) === A.QRProvider.VNPAY && t.jsxs(u, {
                                mb: 4,
                                children: [t.jsx(u, {
                                    children: t.jsx(e5, {
                                        data: c
                                    })
                                }), t.jsx(u, {
                                    mb: 6
                                }), t.jsx(p1, {}), t.jsx(u, {
                                    mb: 6
                                }), t.jsx(u, {
                                    children: t.jsx(o1, {
                                        size: "small",
                                        children: e("home.vnpay.step2.label")
                                    })
                                })]
                            })
                        })
                    }, A.QRProvider.VNPAY)]
                }), t.jsx(J2, {
                    offset: 16,
                    style: {
                        opacity: B.isFetching ? .5 : 1
                    },
                    children: [z.bidv, z.techcombank, z.tpbank, z.namabank].map(f => t.jsxs(v1, {
                        onClick: () => P(f),
                        children: [t.jsx(u, {
                            mb: 1,
                            flex: !0,
                            justifyContent: "center",
                            alignItems: "center",
                            children: t.jsx(B1, {
                                radius: 4,
                                size: 48,
                                app: f.key
                            })
                        }), t.jsx($, {
                            className: "app-name",
                            size: "xxSmall",
                            children: f.shortName
                        })]
                    }, f.key))
                }), t.jsx(u, {
                    mt: 10
                }), t.jsx(U, {
                    variant: "secondary",
                    fullWidth: !0,
                    onClick: Q,
                    children: "QuÃ©t mÃ£ QR khÃ¡c"
                }), t.jsx(f1, {
                    visible: i,
                    text: "Äang má»Ÿ..."
                })]
            })
        })
    },
    i5 = Z1.map(e => e.key),
    T3 = ({
        app: e
    }) => {
        const {
            t: n
        } = j(), {
            data: i
        } = b1();
        return (i == null ? void 0 : i.type) !== A.QRProvider.VIETQR || !i5.includes(e.key) ? null : t.jsx(s5, {
            children: n("label.autofill")
        })
    },
    j3 = ({
        app: e
    }) => {
        const {
            t: n
        } = j(), {
            data: i
        } = b1();
        return (i == null ? void 0 : i.type) !== A.QRProvider.VIETQR || !i5.includes(e.key) ? null : t.jsx(P3, {
            children: n("label.autofill")
        })
    };
var x2;
const s5 = V.div(x2 || (x2 = k(["\n  position: absolute;\n  top: -1px;\n  left: -1px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  width: 86px;\n  background-color: #3ebb6c;\n  border-radius: 8px 0px;\n  color: white;\n  font-size: 9px;\n  line-height: 12px;\n  padding: 1px 6px;\n  text-transform: uppercase;\n  font-weight: 500;\n"])));
var S2;
const P3 = V(s5)(S2 || (S2 = k(["\n  position: relative;\n  border-radius: 8px;\n  width: auto;\n"]))),
    Q3 = ({
        onClickViewMore: e,
        onClose: n
    }) => {
        const {
            t: i
        } = j();
        return t.jsxs(E3, {
            children: [t.jsxs("div", {
                children: [t.jsx($, {
                    size: "xxSmall",
                    bold: !0,
                    children: i("autofill.bannerTitle")
                }), t.jsx(u, {
                    mb: 1
                }), t.jsxs($, {
                    size: "xxSmall",
                    color: "text-02",
                    children: [t.jsx("span", {
                        children: i("autofill.bannerDesc")
                    }), t.jsxs("span", {
                        style: {
                            color: "#0068FF"
                        },
                        onClick: e,
                        children: [" ", i("autofill.bannerCta")]
                    })]
                })]
            }), t.jsx(u, {
                ml: 3,
                children: t.jsx("div", {
                    onClick: n,
                    children: t.jsx(n1, {
                        icon: "zi-close",
                        size: 16
                    })
                })
            })]
        })
    };
var H2;
const E3 = V.div(H2 || (H2 = k(["\n  background-color: #f0f7ff;\n  padding: 12px;\n  border-radius: 8px;\n  display: flex;\n"]))),
    t1 = 65,
    L3 = e => {
        const {
            apps: n,
            open: i,
            onClose: C,
            onClick: r,
            closeOnSelect: a
        } = e, [s, l] = p.useState(""), [c, d] = p.useState(), {
            unmounted: g,
            props: {
                opacity: I
            }
        } = w1(i, 300), {
            t: y
        } = j(), [m, b] = p.useState(t1), [{
            height: B
        }, S] = u1(() => ({
            height: "0vh",
            config: {
                tension: 280
            }
        }), [i]), M = P2(({
            last: x,
            down: R,
            velocity: [, G],
            direction: [, E],
            movement: [, D],
            tap: s1,
            cancel: c1
        }) => {
            const g1 = window.innerHeight,
                l1 = 100 - m,
                N1 = 100 - (D * 100 / g1 + l1),
                F = Math.max(0, Math.min(100, N1)),
                N = (c == null ? void 0 : c.scrollTop) || 0;
            if (s1 || l1 === 100 && E === -1) {
                c1();
                return
            }
            if (x) switch (!0) {
                case (N <= 0 && E === 1 && F > 80):
                    H(t1);
                    break;
                case (F > t1 && G > 1 && E === -1 || F > 80):
                    H(100);
                    break;
                case (F < t1 && E === 1 || F < 40 && E >= 0):
                    P();
                    break;
                default:
                    H(t1);
                    break
            } else N === 0 && S.start({
                height: "".concat(F, "vh"),
                immediate: R
            })
        }, {
            filterTaps: !0,
            preventScroll: !1
        }), H = p.useCallback(x => {
            S.start({
                height: "".concat(x, "vh")
            }), b(x)
        }, [S]), P = p.useCallback(() => {
            H(0), l(""), C()
        }, [H, C]), Q = p.useCallback(async () => {
            K.clickInputSearch()
        }, []), f = p.useCallback(x => {
            r == null || r(x), a && P()
        }, [a, P, r]), w = p.useMemo(() => {
            if (!s) return n;
            const x = s.toLowerCase();
            return n.filter(R => {
                var E;
                return "".concat(R.name, " ").concat(R.key, " ").concat(R.shortName, " ").concat(R.code, " ").concat((E = R.keywords) != null ? E : "").toLowerCase().includes(x) ? R : !1
            })
        }, [n, s]);
        return p.useEffect(() => {
            i && H(t1)
        }, [i, H]), g ? null : t.jsxs(Z3, {
            children: [t.jsx(D3, {
                style: {
                    opacity: I
                },
                onClick: P
            }), t.jsx(z3, {
                children: t.jsxs(Z.div, {
                    ...M(),
                    style: {
                        overflow: "hidden",
                        display: "flex",
                        flexDirection: "column",
                        height: B,
                        touchAction: "none"
                    },
                    children: [t.jsx(Q2, {
                        onClick: P
                    }), t.jsx(E2, {}), t.jsx(u, {
                        textAlign: "center",
                        pb: 3,
                        children: t.jsx(L.Title, {
                            children: y("title.btmSheetSearch")
                        })
                    }), t.jsx(G3, {}), t.jsx(u, {
                        p: 4,
                        style: {
                            position: "relative"
                        },
                        children: t.jsx(K1.Search, {
                            clearable: !0,
                            size: "small",
                            type: "text",
                            id: "search-input",
                            placeholder: y("input.typeYourBank"),
                            onFocus: Q,
                            value: s,
                            onChange: x => l(x.target.value)
                        })
                    }), t.jsxs(U3, {
                        ref: x => d(x),
                        style: {
                            overflowY: m > t1 ? "auto" : "hidden"
                        },
                        children: [w.length === 0 && t.jsx(u, {
                            textAlign: "center",
                            p: 4,
                            children: t.jsx(L, {
                                className: "zaui-text-02",
                                children: y("message.noBankResults")
                            })
                        }), t.jsx(e1, {
                            divider: !0,
                            children: w.map(x => {
                                var R;
                                return t.jsxs(e1.Item, {
                                    className: "zaui-list-item-ellipsis zaui-list-item-pressable",
                                    onClick: () => f(x),
                                    prefix: t.jsx(B1, {
                                        radius: 8,
                                        size: 40,
                                        app: x.key
                                    }),
                                    children: [t.jsx("div", {
                                        className: "zaui-list-item-title-container",
                                        children: t.jsxs($3, {
                                            className: "zaui-list-item-title",
                                            children: [t.jsx("span", {
                                                style: {
                                                    marginRight: "4px"
                                                },
                                                children: x.shortName
                                            }), " ", t.jsx(j3, {
                                                app: x
                                            })]
                                        })
                                    }), t.jsx("div", {
                                        className: "zaui-list-item-subtitle",
                                        children: (R = x.name) == null ? void 0 : R.replace(/NgÃ¢n hÃ ng/g, "NH").replace(/Chi nhÃ¡nh TP\. Há»“ ChÃ­ Minh/g, "CN TP.HCM").replace(/Chi nhÃ¡nh/g, "CN").replace(/ThÆ°Æ¡ng máº¡i/g, "TM")
                                    })]
                                }, x.key)
                            })
                        })]
                    })]
                })
            })]
        })
    };
var I2;
const Z3 = V.div(I2 || (I2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  max-height: 100vh;\n  z-index: 1000;\n"])));
var y2;
const D3 = V(Z.div)(y2 || (y2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  top: 0;\n  background-color: rgba(0, 0, 0, 0.5);\n"])));
var M2;
const z3 = V(Z.div)(M2 || (M2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  background-color: white;\n  border-top-right-radius: 16px;\n  border-top-left-radius: 16px;\n  box-shadow: 0px -2px 6px rgba(20, 20, 21, 0.14);\n"])));
var v2;
const U3 = V.div(v2 || (v2 = k(["\n  height: 100%;\n  overflow-x: hidden;\n  overflow-y: auto;\n  -webkit-overflow-scrolling: touch;\n"])));
var _2;
const $3 = V.div(_2 || (_2 = k(["\n  display: flex;\n  align-items: center;\n"])));
var K2;
const G3 = V.div(K2 || (K2 = k(["\n  height: 1px;\n  width: 100%;\n  background-color: #0000001a;\n"]))),
    W3 = e => {
        const {
            title: n,
            children: i,
            open: C,
            onClose: r,
            divider: a,
            initialHeight: s = 65,
            maxHeight: l = 100
        } = e, {
            unmounted: c,
            props: {
                opacity: d
            }
        } = w1(C, 300), [g, I] = p.useState(s), [{
            height: y
        }, m] = u1(() => ({
            height: "0vh",
            config: {
                tension: 280
            }
        }), [C]), b = P2(({
            last: M,
            down: H,
            velocity: [, P],
            direction: [, Q],
            movement: [, f],
            tap: w,
            cancel: x
        }) => {
            const R = window.innerHeight,
                G = 100 - g,
                E = 100 - (f * 100 / R + G),
                D = Math.max(0, Math.min(100, E));
            if (w || G === 100 && Q === -1) {
                x();
                return
            }
            if (M) switch (!0) {
                case (Q === 1 && D > 80):
                    B(s);
                    break;
                case (D > s && P > 1 && Q === -1 || D > 80):
                    B(l);
                    break;
                case (D < s && Q === 1 || D < 40 && Q >= 0):
                    S();
                    break;
                default:
                    B(s);
                    break
            } else m.start({
                height: "".concat(D, "vh"),
                immediate: H
            })
        }, {
            filterTaps: !0,
            preventScroll: !1
        }), B = p.useCallback(M => {
            m.start({
                height: "".concat(M, "vh")
            }), I(M)
        }, [m]), S = p.useCallback(() => {
            B(0), r()
        }, [B, r]);
        return p.useEffect(() => {
            C && B(s)
        }, [C, B, s]), c ? null : t.jsxs(F3, {
            children: [t.jsx(q3, {
                style: {
                    opacity: d
                },
                onClick: S
            }), t.jsx(X3, {
                children: t.jsxs(Z.div, {
                    ...b(),
                    style: {
                        overflow: "hidden",
                        display: "flex",
                        flexDirection: "column",
                        height: y,
                        touchAction: "none"
                    },
                    children: [t.jsx(Q2, {
                        onClick: S
                    }), t.jsx(E2, {}), t.jsx(u, {
                        textAlign: "center",
                        pb: 3,
                        children: t.jsx(L.Title, {
                            children: n
                        })
                    }), t.jsxs("div", {
                        children: [a && t.jsx(Y3, {}), i]
                    })]
                })
            })]
        })
    };
var w2;
const F3 = V.div(w2 || (w2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  max-height: 100vh;\n  z-index: 1000;\n"])));
var R2;
const q3 = V(Z.div)(R2 || (R2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  top: 0;\n  background-color: rgba(0, 0, 0, 0.5);\n"])));
var O2;
const X3 = V(Z.div)(O2 || (O2 = k(["\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  background-color: white;\n  border-top-right-radius: 16px;\n  border-top-left-radius: 16px;\n  box-shadow: 0px -2px 6px rgba(20, 20, 21, 0.14), 0px 2px 0px rgb(255 255 255);\n"])));
var T2;
const Y3 = V.div(T2 || (T2 = k(["\n  height: 1px;\n  width: 100%;\n  background-color: #0000001a;\n"]))),
    J3 = ({
        open: e,
        onClose: n
    }) => {
        const {
            t: i
        } = j(), [C, r] = p.useState(0);
        return t.jsx(W3, {
            title: i("autofill.btmSheetTitle"),
            open: e,
            onClose: n,
            divider: !0,
            maxHeight: C,
            initialHeight: C,
            children: t.jsx("div", {
                ref: a => {
                    if (a) {
                        const s = window.innerHeight,
                            l = 60,
                            c = a.clientHeight + l,
                            d = Math.min(c * 100 / s, 100);
                        r(d)
                    }
                },
                children: t.jsxs(u, {
                    px: 4,
                    py: 6,
                    children: [t.jsx($, {
                        size: "xSmall",
                        children: i("autofill.btmShetDescLine1")
                    }), t.jsx(u, {
                        mb: 4
                    }), t.jsx($, {
                        size: "xSmall",
                        children: t.jsx("div", {
                            dangerouslySetInnerHTML: {
                                __html: i("autofill.btmShetDescLine2", {
                                    banks: "<strong>".concat(Z1.map(a => a.shortName).join(", "), "</strong>")
                                })
                            }
                        })
                    }), t.jsx(u, {
                        mb: 6
                    }), t.jsx(U, {
                        fullWidth: !0,
                        onClick: n,
                        children: i("button.gotIt")
                    })]
                })
            })
        })
    },
    e6 = (e, n) => {
        const {
            data: i,
            isLoading: C,
            fetchStatus: r,
            ...a
        } = V1(["bankLookup", e], () => c3({
            bin: e.bankBin,
            accountNumber: e.accountNumber
        }), {
            enabled: !!e.bankBin && !!e.accountNumber,
            ...n
        });
        return {
            bankAccountName: i == null ? void 0 : i.data.accountName,
            isLoading: C && r !== "idle",
            ...a
        }
    },
    n6 = e => {
        const [n, i] = p.useState(null), C = p.useMemo(() => e === A.QRProvider.VIETQR ? z : J, [e]), r = p.useMemo(() => {
            const s = i1.getItem(A1);
            return (s ? s.split(",") : []).map(c => C[c]).filter(c => c)
        }, [C]), a = p.useCallback(s => {
            const l = C[s];
            if (l) {
                const c = [l, ...(n != null ? n : []).filter(d => d.key !== s)];
                i(c), i1.setItem(A1, c.map(d => d.key).join(","))
            }
        }, [C, n]);
        return p.useEffect(() => {
            !n && e && i(r)
        }, [n, e, r]), {
            data: n,
            addRecentApp: a
        }
    },
    t6 = e => {
        const {
            data: n,
            ...i
        } = V1(["bankLookup", e], () => l3(), {
            enabled: !!e.type
        }), C = p.useMemo(() => e.type === A.QRProvider.VIETQR ? z : J, [e.type]);
        return {
            data: p.useMemo(() => ((n == null ? void 0 : n.data.banks) || []).map(s => C[s]).filter(s => s), [C, n == null ? void 0 : n.data.banks]) || [],
            ...i
        }
    },
    o6 = (e, n) => {
        const i = new Set;
        return e.filter(C => {
            const r = C[n];
            return i.has(r) ? !1 : i.add(r)
        })
    },
    i6 = () => {
        var g1, l1, N1, F;
        const {
            t: e
        } = j(), n = d1();
        h1(e("header.home")), p.useState(!1);
        const [i, C] = p.useState(!1), [r, a] = p.useState(!1), {
            data: s,
            isSupported: l,
            qrContent: c
        } = b1(), d = Z2(), g = L2(), {
            data: I,
            addRecentApp: y
        } = n6(s == null ? void 0 : s.type), {
            data: m,
            isLoading: b
        } = t6({
            type: s == null ? void 0 : s.type
        }), {
            openApp: B
        } = F2(), {
            bankAccountName: S,
            isLoading: M
        } = e6({
            bankBin: (g1 = s == null ? void 0 : s.bank) != null && g1.lookupSupported && (N1 = (l1 = s == null ? void 0 : s.bank) == null ? void 0 : l1.bin) != null ? N1 : "",
            accountNumber: (F = s == null ? void 0 : s.bankNumber) != null ? F : ""
        }, {
            onSuccess: () => {
                var N;
                K.lookupBankAccountNameSuccess({
                    bank: (N = s == null ? void 0 : s.bank) == null ? void 0 : N.key
                })
            }
        }), H = p.useCallback(N => {
            var W;
            return m3.includes((W = s == null ? void 0 : s.bank) == null ? void 0 : W.key) ? N.filter(q => q.key !== a1.key) : N
        }, [s]), P = p.useMemo(() => {
            const N = (s == null ? void 0 : s.type) === A.QRProvider.VIETQR ? t5 : o5;
            return H(N)
        }, [s, H]), Q = p.useMemo(() => {
            const N = (s == null ? void 0 : s.type) === A.QRProvider.VIETQR ? K3 : w3;
            return H(N)
        }, [s, H]), f = p.useMemo(() => o6([...H(Y() ? I || [] : []), ...H(m), ...Q].filter(N => N), "key").slice(0, 4), [I, H, m, Q]), w = p.useCallback((N, W) => {
            if (N.type === "bank" && B(N, {
                    onSuccess: q => {
                        K.openBankingAppSuccess({
                            bank: N.key,
                            type: s == null ? void 0 : s.type,
                            src: W
                        }), q != null && q.openStore || y(N.key)
                    },
                    onError: () => {
                        n.openSnackbar({
                            text: e("message.cannotOpenBankingApp"),
                            type: "warning"
                        })
                    }
                }), N.key === a1.key) {
                const q = "".concat(a1.openUrl).concat(encodeURI(c != null ? c : ""));
                window.location.href = q, K.openBankingAppSuccess({
                    bank: N.key,
                    type: s == null ? void 0 : s.type,
                    src: W
                }), y(N.key)
            }
        }, [y, s == null ? void 0 : s.type, B, n, e, c]), x = p.useCallback(N => {
            K.clickItemBankingApp({
                src: "home",
                type: s == null ? void 0 : s.type,
                bank: N.key
            }), w(N, "home")
        }, [w, s]), R = p.useCallback(N => {
            K.clickItemBankingApp({
                src: "btm_sheet",
                type: s == null ? void 0 : s.type,
                bank: N.key
            }), w(N, "btm_sheet")
        }, [w, s]), G = p.useCallback(() => {
            K.clickBtnViewAll(), C(!0)
        }, []), E = () => {
            K.clickIconShowAutofill(), a(!0)
        }, D = () => {
            K.clickCloseBannerAutofill(), g.closeBannerAutofill()
        }, s1 = () => {
            K.clickBannerShowAutofill(), a(!0)
        }, c1 = p.useMemo(() => M || b ? [] : f.filter(N => Z1.find(W => W.key === N.key)), [f, M, b]);
        return j1(() => {
            var W;
            const N = {
                type: s == null ? void 0 : s.type,
                amount: s != null && s.amount ? 1 : 0,
                content: s != null && s.content ? 1 : 0
            };
            (s == null ? void 0 : s.type) === A.QRProvider.VIETQR && (N.bank = (W = s == null ? void 0 : s.bank) == null ? void 0 : W.key, N.bankNumber = s.bankNumber ? 1 : 0), (s == null ? void 0 : s.type) === A.QRProvider.VNPAY && (N.store = s.store ? 1 : 0, N.terminal = s.terminal ? 1 : 0), s != null && s.amount && (N.amount = s.amount), c1.length > 0 && (N.listPartner = c1.map(q => q.key)), K.pageLoadDone(N)
        }, !!(l && s && !b)), l ? (s == null ? void 0 : s.type) === A.QRProvider.VIETQR && M || b ? t.jsx(X, {
            children: t.jsx(f1, {
                visible: !0
            })
        }) : t.jsx(X, {
            children: t.jsxs(r1, {
                children: [(s == null ? void 0 : s.type) === A.QRProvider.VIETQR && t.jsxs(u, {
                    mb: 4,
                    children: [t.jsx(u, {
                        mb: 4,
                        children: t.jsx(L.Title, {
                            size: "small",
                            children: e("home.vietqr.step1.label")
                        })
                    }), t.jsx(u, {
                        children: t.jsx(L1, {
                            data: s,
                            bankAccountName: S
                        })
                    }), t.jsx(u, {
                        mb: 6
                    }), t.jsx(p1, {}), t.jsx(u, {
                        mb: 6
                    }), t.jsx(u, {
                        children: t.jsxs(L.Title, {
                            size: "small",
                            style: {
                                whiteSpace: "pre-wrap"
                            },
                            children: [e("home.vietqr.step2.label"), t.jsx("span", {
                                className: "zaui-text-02",
                                children: t.jsx(s6, {
                                    onClick: E,
                                    children: t.jsx(n1, {
                                        icon: "zi-info-circle",
                                        size: 16
                                    })
                                })
                            })]
                        })
                    })]
                }), (s == null ? void 0 : s.type) === A.QRProvider.VNPAY && t.jsxs(u, {
                    mb: 4,
                    children: [t.jsx(u, {
                        children: t.jsx(e5, {
                            data: s
                        })
                    }), t.jsx(u, {
                        mb: 6
                    }), t.jsx(p1, {}), t.jsx(u, {
                        mb: 6
                    }), t.jsx(u, {
                        children: t.jsx(L.Title, {
                            size: "small",
                            children: e("home.vnpay.step2.label")
                        })
                    })]
                }), t.jsx(u, {
                    mb: 4,
                    children: t.jsxs(J2, {
                        offset: 16,
                        children: [f.map(N => t.jsxs(v1, {
                            onClick: () => x(N),
                            children: [t.jsx(T3, {
                                app: N
                            }), t.jsx(u, {
                                mb: 1,
                                flex: !0,
                                justifyContent: "center",
                                alignItems: "center",
                                children: t.jsx(B1, {
                                    radius: 4,
                                    size: 48,
                                    app: N.key
                                })
                            }), t.jsx(L, {
                                className: "app-name",
                                size: "xxSmall",
                                children: N.shortName
                            })]
                        }, N.key)), t.jsxs(v1, {
                            onClick: G,
                            children: [t.jsx(u, {
                                mb: 1,
                                height: 48,
                                flex: !0,
                                justifyContent: "center",
                                alignItems: "center",
                                children: t.jsx(n1, {
                                    icon: "zi-more-grid",
                                    className: "zaui-text-02"
                                })
                            }), t.jsx(L, {
                                size: "xxSmall",
                                children: e("button.viewAll")
                            })]
                        })]
                    })
                }), c1.length > 0 && !d && t.jsxs(t.Fragment, {
                    children: [t.jsx(Q3, {
                        onClickViewMore: s1,
                        onClose: D
                    }), t.jsx(u, {
                        mb: 4
                    })]
                }), t.jsx(u, {
                    children: t.jsx(X2, {
                        src: "home",
                        type: s == null ? void 0 : s.type,
                        bankAccountName: S
                    })
                }), t.jsx(L3, {
                    apps: P,
                    open: i,
                    onClose: () => C(!1),
                    onClick: R,
                    closeOnSelect: !0
                }), t.jsx(J3, {
                    open: r,
                    onClose: () => a(!1)
                })]
            })
        }) : t.jsx(X, {
            children: t.jsx(D2, {})
        })
    };
var j2;
const s6 = V.span(j2 || (j2 = k(["\n  box-sizing: border-box;\n  border-radius: 4px;\n  display: inline-flex;\n  padding: 1px;\n  margin-left: 4px;\n  transform: translateY(1px);\n  &:active {\n    background-color: var(--zmp-pressed-bg-color);\n  }\n"]))),
    C6 = new b5({
        defaultOptions: {
            queries: {
                retry: !1,
                refetchOnWindowFocus: !1
            }
        }
    }),
    a6 = () => t.jsx(g5, {
        children: t.jsx(N5, {
            client: C6,
            children: t.jsx(k5, {
                children: t.jsx(V5, {
                    basename: "/banking",
                    children: t.jsx(b3, {
                        children: t.jsxs(A5, {
                            children: [t.jsx(C1, {
                                path: "/",
                                element: t.jsx(i6, {})
                            }), t.jsx(C1, {
                                path: "/momo",
                                element: t.jsx(H3, {})
                            }), t.jsx(C1, {
                                path: "/dev",
                                element: t.jsx(z5, {})
                            }), t.jsx(C1, {
                                path: "/uat",
                                element: t.jsx(O3, {})
                            }), t.jsx(C1, {
                                path: "/napas-demo",
                                element: t.jsx(M3, {})
                            }), t.jsx(C1, {
                                path: "/feedback/bank-card-csc",
                                element: t.jsx(n3, {})
                            })]
                        })
                    })
                })
            })
        })
    });
const F1 = document.getElementById("app");
F1 && f5.createRoot(F1).render(t.jsx(B5.StrictMode, {
    children: t.jsx(a6, {})
}));
export {
    c6 as __vite_legacy_guard
};