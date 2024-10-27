from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():
    
    with sync_playwright() as p:
        
        checkin_date = '2024-10-27'
        checkout_date = '2024-10-28'
        
        page_url = f'https://www.booking.com/searchresults.es.html?label=gen173nr-1BCAEoggI46AdIM1gEaLEBiAEBmAEKuAEXyAEM2AEB6AEBiAIBqAIDuAKcsvK4BsACAdICJGI4ZDg5YzVmLTVmNmItNDMwNC1hODNmLWQ0MmE5MjllZjRjYdgCBeACAQ&sid=442c26c6bb2be506f52ff36fee5e9cef&aid=304142&checkin={checkin_date}&checkout={checkout_date}&dest_id=-372490&dest_type=city&order=popularity&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&highlighted_hotels=91162&previous_search_id=59000928-6ce1-4124-b878-5ce556dba3aa'

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)
        
        hotels_list = []
        
        # Scroll hacia abajo hasta obtener al menos 120 resultados
        while len(hotels_list) < 120:
            page.mouse.wheel(0, 10000)
            time.sleep(2)
            
            # Selecciona todos los hoteles en la página visible después de cada scroll
            hotels = page.locator('//div[@data-testid="property-card"]').all()
            print(f'Hoteles encontrados hasta ahora: {len(hotels)}')
            
            # Recorre los hoteles y guarda solo los nuevos
            for hotel in hotels[len(hotels_list):120]:  # Limita hasta un máximo de 120 resultados
                hotel_dict = {}
                hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
                hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
                hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
                hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
                hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]
                
                hotels_list.append(hotel_dict)
                
                # Rompe el ciclo si se alcanzan los 120 hoteles
                if len(hotels_list) >= 120:
                    break
        
        df = pd.DataFrame(hotels_list)
        
        # Guarda en CSV
        df.to_csv('hoteles_barcelona.csv', index=False) 
        
        browser.close()
            
if __name__ == '__main__':
    main()

